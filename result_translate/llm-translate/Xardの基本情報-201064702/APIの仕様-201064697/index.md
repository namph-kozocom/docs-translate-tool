Xardの各種業務を行うには、APIを使用します。APIを実行する場合は、APIのリファレンス「API-DOC」を参照してください。

「API-DOC」のURL、ログインID、パスワードは、以下のとおりです。

**URL**

[https://api-doc.connect.xard.jp/](https://api-doc.connect.xard.jp/)

**ログインID**

xard

**パスワード**

infinite-curiosity

*   Xardでは登録／更新処理が非同期で稼働しており、一時的に負荷の高い状況下などでは処理完了までに時間がかかることがございます。  
    たとえば、[Business作成](https://api-doc.connect.xard.jp/#operation/createBusiness)後の[Business取得](https://api-doc.connect.xard.jp/#operation/getBusiness)や[User作成](https://api-doc.connect.xard.jp/#operation/createUser)の処理など、処理タイミングによっては、対象データが存在せずエラーとなるケースがございます。
    
*   システム設計時には、リトライ処理をご検討いただきますようお願いいたします。