本マニュアル là tài liệu hướng dẫn cho các đối tác sử dụng Xard để thực hiện kết nối API và các hoạt động khác.

Người dùng mục tiêu, cấu trúc và cách đọc của tài liệu này như sau:

1.  [Người dùng mục tiêu](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/204603657#1.-%E5%AF%BE%E8%B1%A1%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC)
    
2.  [Cấu trúc tài liệu](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/204603657#2.-%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB%E6%A7%8B%E6%88%90)
    
3.  [Cách đọc tài liệu](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/204603657#3.-%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A2%E3%83%AB%E3%81%AE%E8%AA%AD%E3%81%BF%E6%96%B9)
    
4.  [Về nhãn hiệu](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/204603657#4.-%E5%95%86%E6%A8%99%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)
    

* * *

## 1\. Người dùng mục tiêu

本マニュアル được thiết kế dành cho các đối tác thực hiện xây dựng môi trường và kết nối API của Xard, nhằm giải thích cách thức triển khai Xard.

* * *

## 2\. Cấu trúc tài liệu

本マニュアル được cấu trúc thành các chương sau:

[Giới thiệu](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201327282)

Giải thích tổng quan dịch vụ của Xard và thông tin cơ bản về tài liệu này.

[Thông tin cơ bản về Xard](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064702/Xard)

Giải thích thông tin cơ bản về Xard như quy trình từ phát hành thẻ đến thanh toán, các thành phần cấu thành Xard, cũng như các đặc điểm của thẻ và API.

[Chuẩn bị để sử dụng API](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064743/API)

Giải thích môi trường mà đối tác sử dụng và chuẩn bị cần thiết để sử dụng API trong mỗi môi trường.

[Giải thích chức năng](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064724)

Giải thích quy trình thực hiện các nghiệp vụ khác nhau với Xard và các API được sử dụng.

[Câu hỏi thường gặp](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201588991)

Giải thích các câu hỏi thường gặp về Xard và câu trả lời của chúng.

* * *

## 3\. Cách đọc tài liệu

Các biểu tượng và thuật ngữ được sử dụng trong tài liệu này có nghĩa như sau:

### Biểu tượng sử dụng trong tài liệu

**Biểu tượng**

**Nội dung**

Những điều phải thực hiện hoặc những điều cần đặc biệt lưu ý được ghi chú ở đây.

Thông tin hữu ích hoặc thông tin bổ sung được ghi chú ở đây.

### Thuật ngữ sử dụng trong tài liệu

**Thuật ngữ**

**Nội dung**

Acquirer

Công ty thẻ thực hiện việc thu nhận và quản lý các cửa hàng liên kết với thương hiệu quốc tế.

Công ty in ấn

Công ty thực hiện in ấn và gửi các tài liệu như thẻ vật lý theo yêu cầu của Xard.

Infcurion

Công ty vận hành Xard.  
Thực hiện xử lý phát hành thẻ của các thương hiệu quốc tế, thanh toán và các quy trình liên quan đến hoạt động phát hành thẻ.

Quốc tế

Công ty vận hành mạng lưới thương hiệu quốc tế.

Cửa hàng liên kết quốc tế

Cửa hàng liên kết với thương hiệu quốc tế mà Xard phát hành thẻ có thể sử dụng.

Thành viên quốc tế (nhà tài trợ BIN)

Công ty thành viên quốc tế cung cấp BIN (Số nhận dạng ngân hàng) hoặc IIN (Số nhận dạng người phát hành) cần thiết để phát hành thẻ quốc tế.

Đối tác

Công ty liên kết nhận dịch vụ của Xard.  
Đối tác thực hiện việc thu nhận người dùng và quản lý thành viên.

Người dùng

Người sử dụng thẻ (pháp nhân, cá nhân kinh doanh hoặc cá nhân) do đối tác thu nhận.

Chuyển đổi thời gian thực

Phương thức xử lý thanh toán mà ở đó đối tác thực hiện quản lý số dư. Nguồn tài trợ độc quyền của đối tác được sử dụng theo thời gian thực trong thanh toán.

* * *

## 4\. Về nhãn hiệu

Về các nhãn hiệu được sử dụng trong tài liệu này, vui lòng xem [tại đây](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/1324810249).