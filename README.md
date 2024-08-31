# 0721 数字论证

复刻自 https://github.com/SonderXiaoming/homo

在其基础上使用正则规范了最后输出的表达式

其中 `dict_gen.py` 用于字典生成，预生成并处理好的结果已包含在 `dict.py` 内，使用时只需要 `dict.py` 和 `yuzu.py`

## 开始使用

```python
from yuzu import yuzu
print(yuzu('2333'))
```

输出：

```python
0+721*(0*7+2+1)+(0+7*21+0+7*(2+1)+0*7+2*1)
```
