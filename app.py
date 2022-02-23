import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def generate(model, tokenizer, category, headline, 
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

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if __name__ == "__main__":
    # Batch modification
    with st.form(key='my_form'):
        print("Loading model...")
        tokenizer = AutoTokenizer.from_pretrained("tuanle/VN-News-GPT2")
        model = AutoModelForCausalLM.from_pretrained("tuanle/VN-News-GPT2").to(device)
        
        print("Model is ready to serve...")
        desc = "Vietnamese News Generative Model - finetuned GPT2"

        st.title('Vietnamese News Generative Model!')
        st.write(desc)
        st.write("##")
        option = st.selectbox(
            'Choose a category',
            ('thời sự ', 'thế giới', 'tài chính kinh doanh', 
            'đời sống', 'văn hoá', 'giải trí', 'giới trẻ', 'giáo dục',
            'công nghệ', 'sức khoẻ'))

        st.write("##")
        category = str(option)
        headline = st.text_input('Headline (or part of the headline)')
        num_return_sequences = st.slider('Number of return sequences', min_value = 1, max_value = 5, value = 2)
        max_len = st.slider('Max Length', min_value = 80, max_value = 768, value = 300)
        with st.expander("Setting parameters"):
            min_len = st.slider('Min Length', min_value = 0, max_value = 50, value = 60)
            top_k = st.slider('Top k', min_value = 30, max_value = 200, value = 50)
            top_p = st.slider('Top p', min_value = 0.0, max_value = 1.0, value = 0.8)
            num_beams = st.slider('Num Beams', min_value = 1, max_value = 6, value = 3)
            

        submit_button = st.form_submit_button(label='Generate', )



        if submit_button:
            print("Generating output")
            with st.spinner('Wait for it...'):
                outputs = generate(model, tokenizer, category = str(category), headline = str(headline), min_len = min_len, max_len = max_len, num_return_sequences = num_return_sequences)

            for i, output in enumerate(outputs):
                # Cut start of text
                temp = output.split("<|startoftext|>")[1].strip()

                temp = temp.split("<|headline|>")
                category = temp[0]

                temp = temp[1].split("<|content|>")
                headline = temp[0].strip()
                content = temp[1].strip()

                st.header(f"Output: {i}")
                st.subheader("Category")
                st.write(category)
                st.subheader(f"Headline")
                st.write(headline)
                st.subheader(f"Content")
                st.write(content)
                st.write("##")

            st.balloons()
