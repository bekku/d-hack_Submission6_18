# d-hack_Submission6_18

# Djangoの初期設定sqlite3からデータ取得
model
```bash
class jsonres_model(models.Model):
    jsonres_nama = models.CharField(blank=False, null=False, max_length=150)
    coment = models.TextField(blank=True)
    age = models.IntegerField(blank=True)
    def __str__(self):
        return self.jsonres_nama
```        
       
view
```bash
model_data = jsonres_model.objects.all()
model_bekku = get_object_or_404(jsonres_model,jsonres_nama="bekku")
user_info = {"login_name": model_bekku.jsonres_nama,
             "age" : model_bekku.age,
             "coment" : model_bekku.coment}
json_item = json.dumps(user_info)
return HttpResponse(json_item)
```

# 結果
```bash
{"login_name": "bekku", "age": 21, "coment": "yahho!"}
```

