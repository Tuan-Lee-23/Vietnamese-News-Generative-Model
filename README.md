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
Categories are:
- thời sự, 'thế giới', 'tài chính kinh doanh', 'đời sống', 'văn hoá', 'giải trí', 'giới trẻ', 'giáo dục', 'công nghệ', 'sức khoẻ'

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
- Example result
![image](https://user-images.githubusercontent.com/43035837/155842166-6ebf4fe1-0470-4fad-8c0b-0c50e821f310.png)
- Input:
```
  - Category: thế giới
  - Headline: Chiến tranh biên giới
```
- Output:

- Article 1:
  - Headline: Chiến tranh biên giới Nga - phương Tây căng thẳng
  - Content: 

Hôm qua (24.11), Mỹ và các đồng minh bày tỏ lo ngại về khả năng Nga tấn công Ukraine, trong khi Moscow bác bỏ cáo buộc này.

Reuters dẫn lời các quan chức Mỹ cho rằng Nga có thể tiến hành chiến tranh với Ukraine trong vài ngày tới. Trong khi đó, Bộ trưởng Quốc phòng Nga Sergei Shoigu tuyên bố Nga không đe dọa bất kỳ ai. Ông lặp lại lời kêu gọi NATO không mở rộng về phía đông, đồng thời cho biết Nga sẵn sàng đối thoại với các nước châu Âu và châu lục địa để giải quyết các vấn đề an ninh và ổn định ở châu Á - Thái Bình Dương (Indo-Pacific).

Trong khi các cuộc đàm phán diễn ra trong bối cảnh Nga tập trung hàng chục ngàn binh sĩ gần biên cương của mình, Moscow phủ nhận các yêu cầu của Mỹ về việc rút quân khỏi Ukraine. Tuy nhiên, Tổng thống Ukraine Volodymyr Zelensky của Ukraine cho hay nước này không có ý định nhượng bộ về lãnh thổ nước mình. “Chúng tôi không lo lắng về các lệnh cấm vận”, ông phát biểu tại cuộc họp báo ở thủ đô Kiev hôm qua. Nhà lãnh đạo Ukraine cũng nói rằng các hoạt động quân sự của Nga tại khu vực đang trở nên tồi tệ hơn so với những gì Moscow từng thực hiện gần đây. Nga đã nhiều lần cảnh báo các lực lượng vũ trang Ukraine và NATO về những hành động tương tự, dù Moscow không đưa ra bình luận chính thức. Giới quan sát trước đó lo sợ Nga sẽ đưa quân đến gần Ukraine nếu có động thái gây bất ổn. Tổng thư ký NATO Jens Stoltenberg ngày 26.10 cho thấy Nga đang chuẩn bị cho một cuộc tập trận chung với Mỹ trong tuần này, theo Reuters. Một phát ngôn viên Bộ Ngoại giao Nga Maria Zakharova ngày 24.9 nói Moscow đang xem xét việc triển khai thêm vũ khí hạt nhân và tên lửa đạn đạo tầm trung (IRBM) đến Đông Âu, châu Phi và Trung Đông để đối phó với sự trỗi dậy của biến thể Omicron. Trước đó một ngày, Nga thông báo đã thử nghiệm thành công một hệ thống IRBM mới, nhưng chưa có thông tin về phản ứng của Moscow đối với đề xuất này từ phía Mỹ. Moscow khẳng định các máy bay không người lái (UAV) do Nga chế tạo đều có hiệu lực tốt và được bảo vệ bởi các cơ quan tình báo quốc tế. Hồi tháng trước, Ukraine đã đưa thêm một số tiêm kích F-16A và Su-30 đến căn cứ không quân ở miền đông Ukraine để phản đối sự bành trướng của quân đội Nga. Đáp lại, chính quyền Kiev ngày 25.12 đã thông qua dự luật cho phép Ukraine sáp nhập bán đảo Crimea vào năm 2014 với giá 1,5 triệu USD. Ngoài ra còn có một thỏa thuận AUKUS với Nga nhằm giúp Ukraine gia nhập NATO. Theo Reuters, Mỹ cũng đã đề nghị Nga cung cấp thêm chi phí cho việc xây dựng cơ sở hạ tầng cho các tàu chiến, tàu hộ tống và tàu tuần tra của NATO tại biên viễn này trong năm nay, nhằm ngăn chặn việc Nga xâm nhập Ukraine từ các bên khác. Ngoại trưởng Mỹ Antony Blinken dự kiến sẽ có cuộc điện đàm với người đồng cấp Nga Vladimir Putin vào ngày 30.1.2022, trước khi cuộc gặp giữa ông Putin và ông Bynic giữa các bộ trưởng Nga và Ukraine sẽ được tổ chức trực tiếp tại Geneva (Thụy Sĩ) vào cuối tháng này (theo giờ địa phương). Các ngoại trưởng cũng có mặt tại Moscow từ ngày 2 - 3.2 để thảo luận về tình hình Ukraine tại Hội nghị thượng đỉnh G20 của Liên Hiệp Quốc về biến đổi khí hậu lần thứ
- Article 2:
  - headline: Chiến tranh biên giới Nga - phương Tây căng thẳng
  - content: 

Trong một diễn biến liên quan tình hình Ukraine, Bộ trưởng Quốc phòng Nga Sergei Shoigu hôm qua thông báo nước này đã tiến hành cuộc tập trận chung với các đồng minh và đối tác ở miền đông Ukraine trong vài ngày qua, theo Reuters. Ông cảnh báo Nga có thể đưa quân lực đến gần lãnh hải của mình, nhưng Moscow đã bác bỏ thông tin này và nhấn mạnh sẽ không đe dọa bất kỳ ai. “Chúng tôi sẵn sàng làm điều đó”, ông phát biểu tại một cuộc họp báo ở thủ đô Moscow hôm 30.11, sau khi Tổng thống Ukraine Volodymyr Zelensky tuyên bố Nga không có ý định xâm lược Ukraine. Nhà lãnh đạo Nga cũng nói thêm rằng những động thái của Nga đối với Ukraine sẽ gây tổn hại đến hòa bình và ổn định ở khu vực, gây thiệt hại nặng nề cho người dân và tài sản của các nước thuộc Liên bang Nga (FSB).

Nga không đưa ra bình luận chính thức nào về những cáo buộc trên. Tuy nhiên, một phát ngôn viên Bộ Ngoại giao Nga cho hay Moscow không vi phạm các lệnh cấm vận của Mỹ và NATO. Ngoại trưởng Ukraine Dmytro Kuleba ngày 29.10 cho biết Nga đã đưa hơn 100.000 binh sĩ và thiết bị quân sự tới gần Ukraine để đối phó khả năng xảy ra xung đột với lực lượng đòi ly khai ở phía đông. Theo Reuters, Nga chưa có phản ứng cụ thể nào từ Washington về các yêu cầu của NATO về việc Ukraine gia nhập liên minh này. Trước đó, NATO đã đề nghị Nga cung cấp vũ khí và khí tài cho Ukraine ngay lập tức, dù Moscow phủ nhận kế hoạch này từ phía Mỹ. Ngày 28.9, Mỹ cho máy bay ném bom B-52 Black Hawk đến căn cứ không quân St. Petersburg để triển khai tên lửa chống tăng và pháo binh. Một quan chức cấp cao trong chính quyền Moscow cũng khẳng định Mỹ sẽ tiếp tục đối thoại với Nga trong những ngày tới, trong bối cảnh Moscow tập trung hàng chục ngàn binh lực ở Ukraine và đang tăng cường các hoạt động ở Đông Âu, châu Á, Thái Bình Dương, Đông Nam Á và châu Phi. Trong khi đó vào ngày 27.8, Tổng thư ký NATO Jens Stoltenberg nói Moscow sẽ làm mọi thứ để đảm bảo an ninh cho tất cả các thành viên của khối, đồng thời bày tỏ hy vọng NATO không mở rộng về phía Nga nếu Moscow có hành động gây bất ổn. Đáp lại, Điện Kremlin nói rằng các cuộc đàm phán về vấn đề Ukraine với Mỹ, EU và các bên khác sẽ được công bố vào tuần tới. Sau khi Nga sáp nhập bán đảo Crimea vào năm 2014, Ukraine đã rút quân khỏi lãnh thổ này trong nhiều tháng để bảo vệ chủ quyền và lợi ích quốc gia. Moscow luôn kiên quyết phản đối các đề xuất của Washington, đặc biệt là việc NATO gia tăng sự hiện diện ở châu Âu. Ngoài ra, Moscow còn kêu gọi NATO giảm các biện pháp hiện đại hóa quân đội và áp đặt các quy định mới để chống lại những nỗ lực của Moscow nhằm vào các nền kinh tế lớn của Ukraine như Trung Quốc, Ấn Độ, Pakistan và thậm chí là Trung Đông. NATO cũng đang tìm cách ngăn chặn sự trỗi dậy của một số nhóm vũ trang mới nổi, chẳng hạn như tổ chức Nhà nước Hồi giáo tự xưng (IS) và al-Qaeda, cũng như các nhóm tội phạm mạng khác. Hồi tháng 9, chính phủ Mỹ thông qua luật cấm nhập cảnh Ukraine cho đến khi có kết quả thẩm định pháp lý. Mỹ cũng đã cấm người nước ngoài đến Ukraine từ ngày 1.1.2022




## Example usage (Huggingface)
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
