Nội dung:

Trong Xard, bạn có thể chọn thông số kỹ thuật của thẻ phát hành. Thông số kỹ thuật của thẻ đã chọn sẽ được đăng ký vào Card Program hoặc Card Product.

1.  [Loại thẻ](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#1.-%E3%82%AB%E3%83%BC%E3%83%89%E3%82%BF%E3%82%A4%E3%83%97)

2.  [Loại kích hoạt](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#2.-%E3%82%A2%E3%82%AF%E3%83%86%E3%82%A3%E3%83%99%E3%83%BC%E3%83%88%E3%82%BF%E3%82%A4%E3%83%97)

3.  [Thiết kế mặt thẻ, bìa, phong bì](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#3.-%E5%88%B8%E9%9D%A2%E3%83%BB%E5%8F%B0%E7%B4%99%E3%83%BB%E5%B0%81%E7%AD%92%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3)

4.  [Phạm vi số thẻ](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#4.-%E3%82%AB%E3%83%BC%E3%83%89%E7%95%AA%E5%8F%B7%EF%BC%88PAN%EF%BC%89%E3%81%AE%E7%AF%84%E5%9B%B2)

5.  [Tỷ lệ phí markup quốc tế và điều kiện thu phí](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#5.-%E6%B5%B7%E5%A4%96%E3%83%9E%E3%83%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%89%8B%E6%95%B0%E6%96%99%E7%8E%87%E3%83%BB%E5%BE%B4%E5%8F%8E%E6%9D%A1%E4%BB%B6)

*   Card Product có thể đăng ký nhiều mục tùy theo nội dung sản phẩm của thẻ.

*   Chỉ có [Tỷ lệ phí markup quốc tế và điều kiện thu phí](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680#4.-%E6%B5%B7%E5%A4%96%E3%83%9E%E3%83%BC%E3%82%AF%E3%82%A2%E3%83%83%E3%83%97%E6%89%8B%E6%95%B0%E6%96%99%E7%8E%87%E3%83%BB%E5%BE%B4%E5%8F%8E%E6%9D%A1%E4%BB%B6) là đăng ký vào Card Program, các mục khác đăng ký vào Card Product.

* * *

## 1\. Loại thẻ

Mỗi Card Product, chọn loại thẻ từ "**Physical**" hoặc "**Virtual**".

**Physical**

*   Gửi thẻ Physical đến người dùng.

*   Loại thẻ Physical có thể chọn một trong các loại sau:

    *   Thẻ IC (thẻ kép IC tiếp xúc/không tiếp xúc)

    *   Thẻ từ

*   Khi tạo thẻ, có thể chọn cài đặt số PIN (mã số cá nhân) bằng cách tự động hoặc thủ công.

* * *

**Trong trường hợp chọn số PIN thủ công**

*   Trước khi cài đặt PIN, đối chiếu với thông tin sau về người dùng mục tiêu để đảm bảo PIN không dễ dàng suy đoán từ thông tin cá nhân:

    *   Ngày sinh, số điện thoại (nhà riêng và di động)

    *   Thông tin cá nhân khác

    *   Kết hợp các mục trên

*   Cài đặt mục PIN với [API "Tạo thẻ"](https://api-doc.connect.xard.jp/#operation/createCard).

*   Để người dùng xác nhận PIN đã đăng ký, thực hiện [API "Lấy PIN"](https://api-doc.connect.xard.jp/#operation/getPin).

*   PIN thuộc phạm vi áp dụng của PCIDSS. Chính sách tuân thủ PCIDSS cần được đối tác xem xét.

**Virtual**

*   Thẻ ảo được tạo ra (thẻ Physical không được tạo).

*   Để người dùng xác nhận thông tin thẻ ảo, thực hiện [API "Lấy thông tin bí mật thẻ"](https://api-doc.connect.xard.jp/#operation/sensitiveData).

* * *

## 2\. Loại kích hoạt

Mỗi Card Product, chọn loại kích hoạt từ "**Cần kích hoạt**" hoặc "**Không cần kích hoạt**".

**Cần kích hoạt**

*   Chỉ có thể chọn khi loại thẻ là "Physical".

*   Mã kích hoạt và mã QR được in trên bìa khi gửi thẻ.

*   Người dùng có thể kích hoạt thẻ theo một trong các cách sau để sử dụng thẻ:

    *   Nhập mã kích hoạt trên màn hình do đối tác cung cấp.

    *   Quét mã QR và xác thực trên màn hình do đối tác cung cấp hiển thị.

**Không cần kích hoạt**

Người dùng có thể sử dụng thẻ mà không cần kích hoạt.

* * *

# 3\. Thiết kế mặt thẻ, bìa, phong bì

Tạo từng mục sau cho mỗi Card Product.

**Thiết kế mặt thẻ Physical**

Thiết kế mặt thẻ Physical. Được tạo theo quy định của thẻ thanh toán quốc tế.  
Cần điều chỉnh thiết kế với công ty in ấn và nhận phê duyệt từ thương hiệu quốc tế cho thiết kế cuối cùng.

**Thiết kế bìa thẻ Physical**

Thiết kế bìa khi gửi thẻ Physical. Điều chỉnh thiết kế với công ty in ấn.

**Thiết kế phong bì thẻ Physical**

Thiết kế phong bì khi gửi thẻ Physical. Điều chỉnh thiết kế với công ty in ấn.

**Thiết kế thẻ cho Widget**

Thiết kế màn hình hiển thị khi người dùng truy vấn thông tin thẻ với tính năng widget thẻ. Được tạo theo quy định cho VirtualAccounts của thương hiệu quốc tế.  
Cần phê duyệt từ thương hiệu quốc tế cho thiết kế cuối cùng.

Cũng có thể tạo leaflet kèm theo khi gửi thẻ Physical.

*   Phương pháp gửi thẻ Physical là qua thư thường hoặc thư bảo đảm đơn giản, có thể chỉ định khi tạo API thẻ.

*   Trong tương lai, dự kiến sẽ hỗ trợ ghi nhận đặc biệt cho bưu phẩm.

* * *

# 4\. Phạm vi số thẻ (PAN)

*   Đặt phạm vi số thẻ để đánh số mỗi khi phát hành thẻ với mỗi CardProduct.

*   Có thể đặt tự do từ số thứ 9 đến số thứ 15 của số thẻ bên phía đối tác.

    *   Từ số 1 đến 8 của số thẻ là BIN của đối tác.

    *   Số thứ 16 của số thẻ là kiểm tra số (check digit).

*   Có thể chia phạm vi số thẻ được chỉ định để sử dụng nhiều CardProduct cho cùng một BIN.

![image-20240304-023832.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-023832.png?api=v2)

Lấy số thẻ ngẫu nhiên từ phạm vi số thẻ đã đăng ký và phát hành số thẻ, một khi đã đặt phạm vi, không thể chia nhỏ phạm vi sau đó.

Để kiểm tra phía Xard, sử dụng khoảng 100 số thẻ ban đầu cho mỗi CardProduct.

Ví dụ) Phương pháp đặt từ số thứ 9 đến số thứ 15

Khi phát hành thẻ vật lý và thẻ ảo với cùng một BIN

**Thẻ vật lý**

![image-20240304-025424.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-025424.png?api=v2)

**Thẻ ảo**

![image-20240304-025617.png](https://infcurion-jira.atlassian.net/wiki/download/attachments/201064680/image-20240304-025617.png?api=v2)

※ Để sử dụng 100 thẻ đầu tiên cho Xard, chỉ định từ 100.

* * *

# 5\. Tỷ lệ phí markup quốc tế và điều kiện thu phí

Đặt từng mục sau cho mỗi Card Program.

**Tỷ lệ phí markup quốc tế**

Đặt tỷ lệ phí markup quốc tế (phí phát sinh khi sử dụng thẻ ở nước ngoài).  
Tỷ lệ phí tiêu chuẩn là 3%, nhưng có thể thiết lập các tỷ lệ khác.  
Có thể đặt tỷ lệ phí đến hai số sau dấu thập phân.

**Điều kiện thu phí markup quốc tế**

Đặt điều kiện để thu phí markup quốc tế. Có thể chọn từ hai mẫu sau.

Mẫu 1:  
Cài đặt tiêu chuẩn của Xard

Thu phí markup quốc tế khi mã tiền tệ khác yên Nhật.

Mẫu 2:  
Cài đặt tùy chọn (theo tiêu chuẩn thương hiệu quốc tế)

Thu phí markup quốc tế khi đáp ứng điều kiện sau.

【Với Visa】

Authorization: Đáp ứng ít nhất một trong các điều kiện ① đến ③ dưới đây và được phán đoán là giao dịch quốc tế  
① Mã quốc gia Acquirer không phải là "Nội địa"  
② Mã quốc gia của cửa hàng thành viên thương hiệu quốc tế không phải là "JP"  
③ Tiền tệ không phải là "Yên Nhật"  
Clearing: Settlement Flag mà Visa chuyển giao không phải là "8 (Nội địa)"

【Với JCB】

Authorization và Clearing: ID trung tâm gửi từ JCB là "1a996610000" (ID giao dịch quốc tế)

Cách xử lý phí markup quốc tế trong trường hợp hoàn trả tại Xard như sau.

   Trường hợp hoàn trả sau khi xác nhận doanh số: Không hoàn trả phí markup quốc tế.

   Trường hợp hủy trước khi xác nhận doanh số: Hoàn trả bao gồm cả phí markup quốc tế.