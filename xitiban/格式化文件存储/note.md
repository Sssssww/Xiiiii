#结构化文件存储
- xml， json
- 为了解决不同设备之间信息交换
- xml
- json
# XML文件
- XML(eXtensibleMarkupLanguage),可扩张语言
    - 标记语言：语言中使用尖括号括起来的文本字符
    - 可扩展:用户可以自己定义需要的标记


            <Teacher>
                自己定义Teacher
                在两个标记之间任何内容都应该跟Teacher有关
            </Teacher>
    - 是w3c组织制定的一个标准
    - XML描述的是数据本身，及数据的结构和语义
    - HTML侧重于如何展示web页面中的数据


- XML文档的构成
    - 处理指令(可以一一个文件内只有一个处理命令)
        - 最多只有行
        - 且必须只有一行
        - 内容是与xml本身处理起一些相关的一些申明或指令
        - 以xml关键字开头
        - 一般用于一些申明XML的版本和采用的编码
            - version属性是必须的
            - encoding属性是用来支出xml解释器使用的编码

    - 根元素(一个文件只有一个跟元素)
        - 在整个xml文件中，可以把他看作一个树形结构
        - 根元素只能有一个
    - 子元素
    - 属性
    - 内容
        - 标签存储的信息
     -注释
        - 其说明作用的信息
        - 注释不能嵌套在标签里
        - 只有在注释的开头和结尾只用双横线
        - 三短横线只能出现在开头

- 保留字符的处理
    - XML中使用的符号可能跟实际符号相冲突，典型的包括左右尖括号
    - 使用实体引用来表示保留字符


    - 把含有保留字符的部分放在CDTA块内部，CDTA块把内部信息视为不需要转义

            <![CDATA[
                select name,age
                from Student
                where socre>8
                ]]>
    -常用的需要转义的保留字符和对应的实体引用
            - & :&amp;
            - < :&lt;
            - > :&gt;
            - " :&apos;
            - ' :&quot;
            - 一共五个，每个实体引用都以&结尾 以分号结尾

- XML标签的命名规则
   - Pascal命名法
   - 用单词表示，第一个字母大写
   - 大小写严格区分
   - 配对的标签必须一致
- 命名空间

    -为了防止命名冲突

            <Student>
                <Name>LiuYing</Name>
                <Age>23</Age>
            </Student>
            <Room>
                <Name>2014</Name>
                <Location>1-23-1</Location>
            </Room>

    - 如果归并上述两个内容信息，会产生冲突

             <Schooler>
                <Name>LiuYing</Name>
                <Age>23</Age>
                <Name>2014</Name>
                <Location>1-23-1</Location>
            </Schooler>
    - 为了避免冲突，需要给可能冲突元素添加命名空间

    - xmlns：xml名称空间的缩写

            <Schooler xmlns:student="http://my_student" xmlns:room="http://my_room">
                <student:Name>LiuYing</student:Name>
                <Age>23</Age>
                <romm:Name>2014</room:Name>
                <Location>1-23-1</Location>
            </Schooler>
# xml的访问

## 读取
- XML读取分两个技术，spa，dom
- SAX(Simple API for XML)
    - 基于事件驱动
    - 利用SAX解析文档设计到解析器和事件处理两部分
    - 特点：
        - 快
        - 流式读取

- DOM
    - 是W3C规定的XML编程接口
    - 一个XML文件在缓存中一树型结构保存，读取
    - 用途:
        - 定位浏览XML任何一个节点的信息
        - 添加删除相应内容
    - minido
        minidom命名
            - minidom.parse（filename）：加载读取的xml文件，文件名也可以是xml代码
            - doc.documentElement：获取XML文档对象，一个XML文件只有一个对于的文档对象
            - node.getAttribute（attr_name）：获取XML节点的属性值
            - node.getElementByTagName（tage_name）：得到一个节点对象集合
            - node.childNodes：得到所有孩子节点
            - node.childNodes [指数] .nodeValue：获取单个节点值
            - node.firstNode：得到第一个节点，等价于node.childNodes [0]
            - node.attributes [tage_name]
            - 案例V01
    - etree
            - 以树形结构来表示的XML
            - root.getiterator：得到相应的可迭代的节点集合
            - root.iter
            - 找到（节点名称）：查找指定节点名称的节点，返回一个节点
            - root.findall（NODE_NAME）：返回多个节点名称的节点
            - node.tag：node对应的tagename
            - node.text：节点的文本值
            - node.attrib：是node的属性的字典类型的内容
            - 案例V02