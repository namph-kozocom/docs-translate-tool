Mối quan hệ giữa các yếu tố tạo nên Xard và hệ thống ID khác nhau tùy thuộc vào việc quản lý số dư được thực hiện bởi đối tác hay bởi Xard.

Nội dung của từng cấu trúc/phần tử như sau:

1. [Để quản lý số dư của đối tác (phương thức chuyển đổi theo thời gian thực)](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/2 01064518/Xard#1.-%E3%83%91%E3%83%BC%E3%83%88%E3%83%8A%E3%83%BC%E3%81%AB%E3%82%88%E3%82%8B%E6%AE%8B% E9%AB%98%E7%AE%A1%E7%90%86%EF%BC%88%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%B9% E3%82%A4%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0%E6%96%B9%E5%BC%8F%EF%BC%89%E3%81%AE%E5%A0%B4%E5%90%88)

2. [Để quản lý số dư bằng Xard](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064518/Xard#2 -


Đối với JCB, việc quản lý số dư bằng Xard sẽ được hỗ trợ trong tương lai. Điều này là không thể vào lúc này.

* * *

##1\. Trong trường hợp quản lý số dư theo đối tác (phương pháp chuyển đổi thời gian thực)

![](/wiki/download/attachments/201064518/XardConfiguration.png?api=v2)

**Đối tác**

Đại diện cho một công ty đối tác sử dụng Xard. "**partner\_id**" được cấp cho mỗi đối tác.

**Chương trình**

Đại diện cho một dịch vụ được điều hành bởi một đối tác. "**program\_id**" được cấp cho mỗi chương trình.

Nhiều chương trình có thể được đăng ký cho một Đối tác.

**Cổng chương trình**

Thể hiện điểm cuối ở phía Đối tác trong chương trình loại quản lý số dư của đối tác. "**program\_gateway\_id**" được cấp cho mỗi chương trình.
Đăng ký một Cổng chương trình cho một Chương trình.

**Nguồn tài trợ**

Đại diện cho nguồn phí cho số dư. "**funding\_source\_id**" sẽ được phát hành cho mỗi Nguồn tài trợ.
Đối với các chương trình loại quản lý số dư của đối tác, một Nguồn tài trợ được đăng ký cho một chương trình.

**Kinh doanh**

Đại diện cho công ty đăng ký tham gia Chương trình. "**business\_id**" được cấp cho mỗi pháp nhân.
Nhiều doanh nghiệp có thể được đăng ký cho một chương trình.

**Người dùng**

Đại diện cho chủ thẻ, chẳng hạn như nhân viên Kinh doanh. "**user\_id**" được cấp cho mỗi Người dùng.
Nhiều người dùng có thể được đăng ký cho một doanh nghiệp.

**Tài khoản**

Đại diện cho tài khoản Doanh nghiệp hoặc Người dùng (thông tin giao dịch). "**account\_id**" sẽ được cấp cho mỗi tài khoản.
Đăng ký một tài khoản cho một doanh nghiệp hoặc người dùng. (Tài khoản sẽ được tạo khi [Doanh nghiệp](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business) và [User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User) được tạo.)

**Sản phẩm thẻ**

Cho biết các thông số kỹ thuật của thẻ được phát hành. "**card\_product\_id**" được phát hành cho từng thông số kỹ thuật của thẻ.
Nhiều Sản phẩm Thẻ có thể được đăng ký cho một Chương trình.

Để biết thêm thông tin về việc đăng ký Sản phẩm Thẻ, hãy xem "[Thông số thẻ](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680)".

**Thẻ**

Đại diện cho một thẻ thuộc sở hữu của người dùng. "**card\_id**" sẽ được phát hành cho mỗi Thẻ.
Nhiều thẻ có thể được đăng ký cho một Người dùng.

**Khách hàng**

Đại diện cho một máy chủ hoặc thiết bị đầu cuối kết nối với Xard. "**client\_id**" và "**client\_secret**" được cấp cho mỗi Khách hàng.
Nhiều Khách hàng có thể được đăng ký cho một Chương trình.

**Móc**

Đại diện cho một sự kiện mà Xard thông báo cho đối tác.
Bạn có thể chọn có nhận thông báo cho từng sự kiện hay không.
Đối với những sự kiện có thể được thông báo, vui lòng tham khảo "[Hook](https://api-doc.connect.xard.jp/#tag/Hook)" trong API-DOC.

* * *

##2\. Để quản lý số dư bằng Xard

![](/wiki/download/attachments/201064518/XardConfiguration-02.png?api=v2)

**Đối tác**

Đại diện cho một công ty đối tác sử dụng Xard. "**partner\_id**" được cấp cho mỗi đối tác.

**Chương trình**

Đại diện cho một dịch vụ được điều hành bởi một đối tác. "**program\_id**" được cấp cho mỗi chương trình.

Nhiều chương trình có thể được đăng ký cho một Đối tác.

**Nguồn tài trợ**

Đại diện cho nguồn phí cho số dư. "**funding\_source\_id**" sẽ được phát hành cho mỗi Nguồn tài trợ.
Trong các chương trình loại Tài khoản ảo, nhiều Nguồn tài trợ có thể được đăng ký cho một Doanh nghiệp hoặc Người dùng.

**Kinh doanh**

Đại diện cho công ty đăng ký tham gia Chương trình. "**business\_id**" được cấp cho mỗi pháp nhân.
Nhiều doanh nghiệp có thể được đăng ký cho một chương trình.

**Người dùng**

Đại diện cho chủ sở hữu thẻ, chẳng hạn như nhân viên Kinh doanh."**user\_id**" được cấp cho mỗi Người dùng.
Nhiều người dùng có thể được đăng ký cho một doanh nghiệp.

**Tài khoản**

Đại diện cho tài khoản Doanh nghiệp hoặc Người dùng (thông tin giao dịch)."**account\_id**" sẽ được cấp cho mỗi tài khoản.
Đăng ký một tài khoản cho một doanh nghiệp hoặc người dùng.
(Tài khoản sẽ được tạo khi [Doanh nghiệp](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382795777/Business) và [User](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/382664770/User) được tạo.)

**Sản phẩm thẻ**

Cho biết các thông số kỹ thuật của thẻ được phát hành."**card\_product\_id**" được phát hành cho từng thông số kỹ thuật của thẻ.
Nhiều Sản phẩm Thẻ có thể được đăng ký cho một Chương trình.

Để biết thêm thông tin về việc đăng ký Sản phẩm Thẻ, hãy xem "[Thông số thẻ](https://infcurion-jira.atlassian.net/wiki/spaces/XardDocs/pages/201064680)".

**Thẻ**

Đại diện cho một thẻ thuộc sở hữu của người dùng."**card\_id**" sẽ được phát hành cho mỗi Thẻ.
Nhiều thẻ có thể được đăng ký cho một Người dùng.

**Khách hàng**

Đại diện cho một máy chủ hoặc thiết bị đầu cuối kết nối với Xard."**client\_id**" và "**client\_secret**" được cấp cho mỗi Khách hàng.
Nhiều Khách hàng có thể được đăng ký cho một Chương trình.

**Móc**

Đại diện cho một sự kiện mà Xard thông báo cho đối tác.
Bạn có thể chọn có nhận thông báo cho từng sự kiện hay không.
Đối với những sự kiện có thể được thông báo, vui lòng tham khảo "[Hook](https://api-doc.connect.xard.jp/#tag/Hook)" trong API-DOC.