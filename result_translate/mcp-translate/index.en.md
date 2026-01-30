Xard's various operations are performed using APIs. When executing an API, please refer to the API reference "API-DOC."

The URL, login ID, and password for "API-DOC" are as follows:

**URL**

[https://api-doc.connect.xard.jp/](https://api-doc.connect.xard.jp/)

**Login ID**

xard

**Password**

infinite-curiosity

* Xard's registration/update processing operates asynchronously, and under temporarily high-load conditions, it may take time to complete processing. For example, after [creating a Business](https://api-doc.connect.xard.jp/#operation/createBusiness), [retrieving a Business](https://api-doc.connect.xard.jp/#operation/getBusiness) or [creating a User](https://api-doc.connect.xard.jp/#operation/createUser), depending on the processing timing, there may be cases where the target data does not exist, resulting in an error.

* When designing the system, please consider retry processing.