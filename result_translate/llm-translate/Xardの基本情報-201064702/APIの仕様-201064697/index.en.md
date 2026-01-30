To perform various Xard operations, use the API. When executing the API, please refer to the API reference "API-DOC."

The URL, login ID, and password for "API-DOC" are as follows.

**URL**

[https://api-doc.connect.xard.jp/](https://api-doc.connect.xard.jp/)

**Login ID**

xard

**Password**

infinite-curiosity

*   In Xard, registration/update processing operates asynchronously, and in temporarily high-load situations, it may take time to complete processing.  
    For example, after [creating Business](https://api-doc.connect.xard.jp/#operation/createBusiness), fetching [Business](https://api-doc.connect.xard.jp/#operation/getBusiness), or processing [create User](https://api-doc.connect.xard.jp/#operation/createUser), depending on the processing timing, there may be cases where the target data does not exist and an error occurs.
    
*   When designing the system, please consider retry processing.