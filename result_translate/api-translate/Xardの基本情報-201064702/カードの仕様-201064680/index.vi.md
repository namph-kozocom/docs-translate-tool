Xard cho phép bạn lựa chọn thông số kỹ thuật của thẻ sẽ được phát hành. Đăng ký thông số kỹ thuật của thẻ đã chọn vào Chương trình thẻ hoặc Sản phẩm thẻ.

1. [Loại thẻ](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#1.-%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97)

2. [Loại kích hoạt](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#2.- %E3%82%A2%E3%82%AF%E3%83%86%E3%82%A3%E3%83%99%E3%83%BC%E3%83%88%E3%82%BF%E3%82%A4%E3%83%97)

3. [Mặt vé/mount/thiết kế phong bì](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#3.-%E5%88%B 8%E9%9D%A2%E3%83%BB%E5%8F%B0%E7%B4%99%E3%83%BB%E5%B0%81%E7%AD%92%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3)

4. [Phạm vi số thẻ](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#4.-%E3 %82%AB%E3%83%BC%E3%83%89%E7%95%AA%E5%8F%B7%EF%BC%88PAN%EF%BC%89%E3%81%AE%E7%AF%84%E5%9B%B2)

5. [Mức phí tăng giá/điều kiện thu phí ở nước ngoài](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#5.-%E6%B5%B7%E5%A4%96%E3%83%9E% E3%83%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%89%8B%E6%95%B0% E6%96%99%E7%8E%87%E3%83%BB%E5%BE%B4%E5%8F%8E%E6%9D%A1%E4%BB%B6)


* Có thể đăng ký nhiều sản phẩm thẻ tùy thuộc vào nội dung sản phẩm của thẻ.

* [Mức phí tăng giá/điều kiện thu phí ở nước ngoài](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#4.-%E6%B5%B7%E5%A4%96%E3%83%9E%E3%8 3%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%89%8B%E6%95%B0%E6%96 %99%E7%8E%87%E3%83%BB%E5%BE%B4%E5%8F%8E%E6%9D%A1%E4%BB%B6), Chương trình Đăng ký Thẻ và các mục khác cho Sản phẩm Thẻ.


* * *

##1\. Loại thẻ

Đối với mỗi Sản phẩm Thẻ, hãy chọn loại thẻ từ "**Vật lý**" hoặc "**Ảo**".

**Vật lý**

* Gửi thẻ vật lý cho người dùng.

*Bạn có thể chọn một trong các loại thẻ vật lý sau.

* Thẻ IC (thẻ kép IC tiếp xúc/không tiếp xúc)

*Thẻ từ

* Khi tạo thẻ, bạn có thể chọn cài đặt mã PIN (Số nhận dạng cá nhân) từ đánh số tự động hoặc đánh số thủ công.


* * *

**Nếu mã PIN được gán thủ công**

* Trước khi đặt mã PIN, đối tác nên kiểm tra các thông tin sau về người dùng mục tiêu để đảm bảo rằng mã PIN không dễ đoán dựa trên thông tin cá nhân.

* Ngày sinh, số điện thoại (nhà và di động)

* Thông tin cá nhân khác

* Sự kết hợp của những điều trên

* Vui lòng đặt các mục PIN bằng cách sử dụng [API “Tạo thẻ”](https://api-doc.connect.xard.jp/#Operation/createCard).

* Để kiểm tra mã PIN đã đăng ký, người dùng nên thực thi [API "Nhận mã PIN"](https://api-doc.connect.xard.jp/#Operation/getPin).

* Mã PIN phải tuân theo PCIDSS. Chúng tôi yêu cầu các đối tác xem xét chính sách tuân thủ PCIDSS.


**Ảo**

* Thẻ ảo được tạo (thẻ vật lý không được tạo).

* Để kiểm tra thông tin thẻ của thẻ ảo, người dùng nên thực thi [API "Truy xuất thông tin thẻ bí mật"](https://api-doc.connect.xard.jp/#Operation/sensitiveData).


* * *

##2\. Loại kích hoạt

Đối với mỗi Sản phẩm Thẻ, hãy chọn loại kích hoạt từ "**Yêu cầu kích hoạt**" hoặc "**Không yêu cầu kích hoạt**".

**Yêu cầu kích hoạt**

* Chỉ có thể chọn khi loại thẻ là "Vật lý".

* Mã kích hoạt và mã QR sẽ được in ở mặt sau khi gửi thẻ.

* Người dùng có thể sử dụng thẻ của mình bằng cách kích hoạt thẻ theo một trong các cách sau:

*Nhập mã kích hoạt trên màn hình do đối tác cung cấp.

* Quét mã QR và xác thực trên màn hình do đối tác cung cấp xuất hiện.


**Kích hoạt/Không bắt buộc**

Người dùng có thể sử dụng thẻ mà không cần kích hoạt.

* * *

# 3\. Thiết kế mặt/gắn thẻ/phong bì thẻ

Tạo từng mục sau cho từng Sản phẩm Thẻ:

**Thiết kế thẻ vật lý**

Đây là thiết kế mặt của lá bài Vật lý. Được tạo ra theo quy định về danh thiếp thương hiệu quốc tế.
Bạn sẽ cần phối hợp thiết kế của mình với công ty in ấn và nhận được sự chấp thuận của thương hiệu quốc tế cho thiết kế cuối cùng của bạn.

**Thiết kế gắn thẻ vật lý**
Đây là thiết kế của vật gắn kết khi gửi thẻ Physical.Phối hợp thiết kế với công ty in ấn.

**Thiết kế phong bì thẻ vật lý**

Đây là thiết kế của phong bì khi gửi thiệp vật lý.Phối hợp thiết kế với công ty in ấn.

**Thiết kế thẻ cho tiện ích thẻ**

Đây là thiết kế màn hình hiển thị khi người dùng truy vấn thông tin thẻ bằng chức năng widget thẻ.Được tạo theo quy định của VirtualAccounts thương hiệu quốc tế.
Thiết kế cuối cùng phải được sự chấp thuận của các thương hiệu quốc tế.

Cũng có thể tạo một tờ rơi để kèm theo khi gửi thẻ vật lý.

* Thẻ vật lý có thể được gửi bằng thư thông thường hoặc thư đăng ký đơn giản, có thể được chỉ định bằng API tạo thẻ.

* Trong tương lai, chúng tôi có kế hoạch hỗ trợ thư đã đăng ký được chỉ định.


* * *

# 4\. Phạm vi số thẻ (PAN)

* Đặt phạm vi số thẻ sẽ được chỉ định khi phát hành thẻ cho từng Sản phẩm Thẻ.

* Đối tác có thể tự do thiết lập số thẻ từ 9 đến 15 chữ số.

* Các chữ số từ 1 đến 8 của số thẻ là BIN của đối tác.

*Chữ số thứ 16 của số thẻ là số kiểm tra.

* Cũng có thể sử dụng cùng một BIN cho nhiều Sản phẩm thẻ bằng cách chia phạm vi số thẻ được chỉ định.


![image-20240304-023832.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-023832.png?api=v2)

Số thẻ được lấy ngẫu nhiên từ dãy số thẻ đã đăng ký và phát hành nên khi đã đặt dãy số thì sau này không thể chia được.

Để thử nghiệm phía Xard, chúng tôi sẽ sử dụng 100 số thẻ đầu tiên cho mỗi Sản phẩm Thẻ.

Ví dụ) Cách đặt 9 đến 15 chữ số

Khi phát hành thẻ vật lý và thẻ ảo có cùng BIN

**Thẻ vật lý**

![image-20240304-025424.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-025424.png?api=v2)

**Thẻ ảo**

![image-20240304-025617.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-025617.png?api=v2)

*100 tờ đầu tiên sẽ được sử dụng trong Xard, vì vậy vui lòng chỉ định từ 100.

* * *

# 5\. Tỷ lệ phí đánh dấu ở nước ngoài/điều kiện thu phí

Đặt các mục sau cho mỗi Chương trình Thẻ.

**Mức phí đánh dấu ở nước ngoài**

Đặt tỷ lệ phần trăm phí cộng thêm ở nước ngoài (phí phát sinh khi sử dụng thẻ của bạn ở nước ngoài).
Tỷ lệ hoa hồng tiêu chuẩn là 3%, nhưng các tỷ lệ phần trăm khác có thể được đặt.
Tỷ lệ hoa hồng có thể được đặt thành hai chữ số thập phân.

**Điều kiện thu phí đánh dấu ở nước ngoài**

Đặt ra các điều kiện để thu phí đánh dấu ở nước ngoài.Bạn có thể chọn từ hai mẫu sau.

Mẫu 1:
Cài đặt tiêu chuẩn Xard

Phí tăng giá ở nước ngoài sẽ được thu nếu mã tiền tệ không phải là Yên Nhật.

Mẫu 2:
Cài đặt tùy chọn (tiêu chuẩn thương hiệu quốc tế)

Phí đánh dấu ở nước ngoài sẽ được thu nếu đáp ứng các điều kiện sau.

[Đối với thị thực]

Ủy quyền: Nếu đáp ứng một hoặc nhiều điều kiện sau từ ① đến ③ và giao dịch được xác định là giao dịch ở nước ngoài.
① Mã quốc gia của người thanh toán không phải là “trong nước”
②Mã quốc gia của cửa hàng thành viên thương hiệu quốc tế không phải là "JP"
③Tiền tệ không phải là "Yên Nhật"
Xóa: Nếu Cờ thanh toán được liên kết từ Visa khác với "8 (nội địa)"

[Đối với JCB]

Ủy quyền, thanh toán bù trừ: Nếu ID trung tâm gửi được liên kết từ JCB là "1a996610000" (*ID cho giao dịch nước ngoài)

Cách Xard xử lý phí cộng thêm ở nước ngoài tại thời điểm hoàn trả như sau.

Khi trả lại hàng sau khi việc bán hàng đã được xác nhận: Phí cộng thêm ở nước ngoài sẽ không được hoàn lại.

Nếu hủy trước khi việc bán hàng được xác nhận: Việc hoàn tiền sẽ được thực hiện bao gồm phí tăng giá ở nước ngoài.