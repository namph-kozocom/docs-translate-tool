APIs are used to perform various Xard tasks.To execute the API, please refer to the API reference "API-DOC".

The URL, login ID, and password for "API-DOC" are as follows.

**URL**

[https://api-doc.connect.xard.jp/](https://api-doc.connect.xard.jp/)

**Login ID**

xard

**Password**

infinite-curiosity

* In Xard, the registration/update process is performed asynchronously, so it may take some time to complete the process under temporarily high load conditions.
For example, depending on the processing timing, such as when processing [Get Business] (https://api-doc.connect.xard.jp/#operation/getBusiness) or [Create User] (https://api-doc.connect.xard.jp/#operation/createUser) after [Create Business] (https://api-doc.connect.xard.jp/#operation/createBusiness), there may be cases where the target data does not exist and an error occurs.

*Please consider retry processing when designing your system.