import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = AutoTokenizer.from_pretrained("tuanle/VN-News-GPT2", cache_dir="cache/")
model = AutoModelForCausalLM.from_pretrained("tuanle/VN-News-GPT2", cache_dir="cache/").to(device)
print("Loading model...")
print("Model is ready to serve...")

def generate(category, headline, 
             min_len = 60, 
             max_len = 768, 
             num_beams = 5, 
             num_return_sequences = 3,
             top_k = 50,
             top_p = 1):
    """
        top_p: If set to float < 1, only the most probable tokens with probabilities that add up to top_p or higher are kept for generation.
        top_k: The number of highest probability vocabulary tokens to keep for top-k-filtering.
        num_beams: Number of beams for beam search. 1 means no beam search.
    """
    text = f"<|startoftext|> {category} <|headline|> {headline}"

    input_ids = tokenizer.encode(text, return_tensors='pt').to(device)

    sample_outputs = model.generate(input_ids,
                                    do_sample=True,
                                    max_length=max_len,
                                    min_length=min_len,
                                    #    temperature = .8,
                                    top_k= top_k,
                                    top_p = top_p,
                                    num_beams= num_beams,
                                    early_stopping= True,
                                    no_repeat_ngram_size= 2  ,
                                    num_return_sequences= num_return_sequences)

    outputs = []
    for i, sample_output in enumerate(sample_outputs):
        temp = tokenizer.decode(sample_output.tolist())
        print(f">> Generated text {i+1}\n\n{temp}")
        print('\n---')
        outputs.append(temp)
    return outputs