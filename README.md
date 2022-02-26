# GPT-2 Fine-tuning With Vietnamese News
## Model description
A Fine-tuned Vietnamese GPT2 model which can generate Vietnamese news based on context (category + headline), based on the Vietnamese Wiki GPT2 pretrained model (https://huggingface.co/danghuy1999/gpt2-viwiki)

## Huggingface hub
- https://huggingface.co/tuanle/VN-News-GPT2

## Purpose
This model was made only for fun and experimental study. However, It gives impressive results
Most of the generative news are fake with unconfirmed information. Honestly, I feel fun about this project =))

## Dataset
The dataset is about 30k Vietnamese news dataset from website thanhnien.vn

## Result  
- Train Loss: 2.3
- Val loss: 2.5
- Rouge F1: 0.556
- Word error rate: 1.08

## Deployment
- You can run the model deployment in this Colab's [link](https://colab.research.google.com/drive/1ITnYPnngd_aqkFB2A5IhzSsX4jQSPOR1?usp=sharing)
- Then go to this link: https://gptvn.loca.lt
- You can choose any categories and give it some text for the headline, then generate. There we go
- P/s: I've already tried to deploy my model on Streamlit's cloud, but It was always being broken due to out of memory


## Example usage
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


"""
Category includes: ['thời sự ', 'thế giới', 'tài chính kinh doanh', 'đời sống', 'văn hoá', 'giải trí', 'giới trẻ', 'giáo dục','công nghệ', 'sức khoẻ']
"""

category = "thời sự"
headline = "Nam thanh niên"  # A full headline or only some text

text = f"<|startoftext|> {category} <|headline|> {headline}"

tokenizer = AutoTokenizer.from_pretrained("tuanle/VN-News-GPT2")
model= AutoModelForCausalLM.from_pretrained("tuanle/VN-News-GPT2").to(device)

input_ids = tokenizer.encode(text, return_tensors='pt').to(device)
sample_outputs = model.generate(input_ids,
                                do_sample=True,
                                max_length= 768,
                                min_length= 60,
                                #    temperature = .8,
                                top_k= 100,
                                top_p = 0.7,
                                num_beams= 5,
                                early_stopping= True,
                                no_repeat_ngram_size= 2  ,
                                num_return_sequences= 3)

for i, sample_output in enumerate(sample_outputs):
    temp = tokenizer.decode(sample_output.tolist())
    print(f">> Generated text {i+1}\n\n{temp}")
    print('\n---')
```
