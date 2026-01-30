Xardを構成する各要素の関係性およびIDの体系は、残高管理をパートナーで行うかXardで行うかによって異なります。

それぞれの構成・要素の内容は以下のとおりです：

1.  [パートナーによる残高管理（リアルタイムスイッチング方式）の場合](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#1.-%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E3%81%AB%E3%82%88%E3%82%8B%E6%AE%8B%E9%AB%98%E7%AE%A1%E7%90%86%EF%BC%88%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0%E6%96%B9%E5%BC%8F%EF%BC%89%E3%81%AE%E5%A0%B4%E5%90%88)
    
2.  [Xardによる残高管理の場合](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#2.-Xard%E3%81%AB%E3%82%88%E3%82%8B%E6%AE%8B%E9%AB%98%E7%AE%A1%E7%90%86%E3%81%AE%E5%A0%B4%E5%90%88)
    

JCBについては、Xardによる残高管理は今後対応予定です。現時点では実施できません。

* * *

## 1\. Quản lý số dư của đối tác (phương thức chuyển đổi thời gian thực)

![](/wiki/download/attachments/201064518/XardConfiguration.png?api=v2)

**Partner**

Biểu thị các công ty đối tác sử dụng Xard. Mỗi đối tác sẽ được cấp một " **partner\_id** ".

**Program**

Biểu thị dịch vụ được điều hành bởi đối tác. Mỗi chương trình sẽ được cấp một " **program\_id** ".

Có thể đăng ký nhiều chương trình cho một đối tác.

**Program Gateway**

Biểu thị đầu mối của phía đối tác trong các chương trình lựa chọn quản lý số dư bởi đối tác. Mỗi chương trình sẽ được cấp một " **program\_gateway\_id** ".  
Đăng ký một Program Gateway cho một chương trình.

**Funding Source**

Biểu thị nguồn nạp số dư. Mỗi nguồn sẽ được cấp một " **funding\_source\_id** ".  
Trong chương trình quản lý số dư của đối tác, đăng ký một Funding Source cho một chương trình.

**Business**

Biểu thị công ty ký hợp đồng tham gia chương trình. Mỗi công ty sẽ được cấp một " **business\_id** ".  
Có thể đăng ký nhiều công ty cho một chương trình.

**User**

Biểu thị chủ sở hữu thẻ, như nhân viên của công ty tham gia Business. Mỗi người dùng sẽ được cấp một " **user\_id** ".  
Có thể đăng ký nhiều người dùng cho một công ty.

**Account**

Biểu thị tài khoản (thông tin giao dịch) của công ty hoặc người dùng. Mỗi tài khoản sẽ được cấp một " **account\_id** ".  
Đăng ký một tài khoản cho một công ty hoặc người dùng. (Tài khoản được tạo tại thời điểm [Business](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business) hoặc [User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User) được tạo).

**Card Product**

Biểu thị thông số kỹ thuật của thẻ được phát hành. Mỗi thông số kỹ thuật thẻ sẽ được cấp một " **card\_product\_id** ".  
Có thể đăng ký nhiều sản phẩm thẻ cho một chương trình.

Về nội dung đăng ký của Card Product, vui lòng tham khảo tại " [カードの仕様](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680) ".

**Card**

Biểu thị thẻ mà người dùng sở hữu. Mỗi thẻ sẽ được cấp một " **card\_id** ".  
Có thể đăng ký nhiều thẻ cho một người dùng.

**Client**

Biểu thị máy chủ hoặc thiết bị kết nối với Xard. Mỗi khách hàng sẽ được cấp một " **client\_id** " và " **client\_secret** ".  
Có thể đăng ký nhiều khách hàng cho một chương trình.

**Hook**

Biểu thị sự kiện thông báo từ Xard đến đối tác.  
Có thể chọn có hoặc không có thông báo cho mỗi sự kiện.  
Các sự kiện có thể thông báo vui lòng tham khảo tại API-DOC " [Hook](https://api-doc.connect.xard.jp/#tag/Hook) ".

* * *

## 2\. Quản lý số dư của Xard

![](/wiki/download/attachments/201064518/XardConfiguration-02.png?api=v2)

**Partner**

Biểu thị các công ty đối tác sử dụng Xard. Mỗi đối tác sẽ được cấp một " **partner\_id** ".

**Program**

Biểu thị dịch vụ được điều hành bởi đối tác. Mỗi chương trình sẽ được cấp một " **program\_id** ".

Có thể đăng ký nhiều chương trình cho một đối tác.

**Funding Source**

Biểu thị nguồn nạp số dư. Mỗi nguồn sẽ được cấp một " **funding\_source\_id** ".  
Trong chương trình kiểu Virtual Account, có thể đăng ký nhiều Funding Source cho một công ty hoặc người dùng.

**Business**

Biểu thị công ty ký hợp đồng tham gia chương trình. Mỗi công ty sẽ được cấp một " **business\_id** ".  
Có thể đăng ký nhiều công ty cho một chương trình.

**User**

Biểu thị chủ sở hữu thẻ, như nhân viên của công ty tham gia Business. Mỗi người dùng sẽ được cấp một " **user\_id** ".  
Có thể đăng ký nhiều người dùng cho một công ty.

**Account**

Biểu thị tài khoản (thông tin giao dịch) của công ty hoặc người dùng. Mỗi tài khoản sẽ được cấp một " **account\_id** ".  
Đăng ký một tài khoản cho một công ty hoặc người dùng.  
(Tài khoản được tạo tại thời điểm [Business](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business) hoặc [User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User) được tạo).

**Card Product**

Biểu thị thông số kỹ thuật của thẻ được phát hành. Mỗi thông số kỹ thuật thẻ sẽ được cấp một " **card\_product\_id** ".  
Có thể đăng ký nhiều sản phẩm thẻ cho một chương trình.

Về nội dung đăng ký của Card Product, vui lòng tham khảo tại " [カードの仕様](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680) ".

**Card**

Biểu thị thẻ mà người dùng sở hữu. Mỗi thẻ sẽ được cấp một " **card\_id** ".  
Có thể đăng ký nhiều thẻ cho một người dùng.

**Client**

Biểu thị máy chủ hoặc thiết bị kết nối với Xard. Mỗi khách hàng sẽ được cấp một " **client\_id** " và " **client\_secret** ".  
Có thể đăng ký nhiều khách hàng cho một chương trình.

**Hook**

Biểu thị sự kiện thông báo từ Xard đến đối tác.  
Có thể chọn có hoặc không có thông báo cho mỗi sự kiện.  
Các sự kiện có thể thông báo vui lòng tham khảo tại API-DOC " [Hook](https://api-doc.connect.xard.jp/#tag/Hook) ".