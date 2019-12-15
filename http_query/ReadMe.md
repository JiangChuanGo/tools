# Install

1. how it looks like

![img](https://raw.githubusercontent.com/JiangChuanGo/imgbed/master/2019/12/screen_cap.png)

2. clone this repo
  ```bash
  git clone https://github.com/JiangChuanGo/tools.git 
  ```

3. pip install requirements.txt
  ```bash
  cd tools/http_query/
  pip install -r requirements.txt
  ```

4. run the tool
  ```bash
  python main.py
  ```

# Usage

1. The **Headers** box should be Empty or filled with Json data like this:
```json
{
    "header_name" : "header_value",
    "Content-length" : "16",
    "Cookies" : ["abc", "123", "456"]
}
```.

2. Data in the **Body** box will be puted into right the HTTP protocol BODY,trictly!

3. The Body Box **only** avilibal with **POST** method.
