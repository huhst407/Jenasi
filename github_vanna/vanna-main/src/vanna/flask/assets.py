html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jenasi.AI</title>
    <link rel="icon" type="image/png" href="https://s2.loli.net/2024/11/22/x9I4JoySjMmu2VZ.png" type="image/x-icon"/>
    <link rel="stylesheet" href="/assets/index-f228f78f.css">
</head>
<body>
    <div class="layout">
        <!--侧边栏-->
        <div class="sidebar">
            <!--添加logo-->
            <img src="https://s2.loli.net/2024/11/22/x9I4JoySjMmu2VZ.png" alt="Jenasi.AI Logo" class="sidebar-logo">
            <h2>Jenasi.AI</h2>
            <ul>
                <li><button id="functionsButton">Functions</button></li>
                <li><button id="trainingDataButton">Training Data</button></li>
                <li><button id="newQuestion">New Question</button></li>
            </ul>
            <button id="signOut">Sign out</button>
        </div>

        <!--主要内容-->
        <div class="main-content">
            <header>
                <h1>Welcome to Jenasi.AI</h1>
                <p>Your AI-powered copilot for SQL queries.</p>

                <!-- 移动这段内容到标题下方 -->
                <section id="exampleQuestions">
                    <h3>Here are some questions you can ask:</h3>
                    <ul>
                        <li><button>What are the top 10 artists by sales?</button></li>
                        <li><button>What are the total sales per year by country?</button></li>
                        <li><button>Who is the top selling artist in each genre? Show the sales numbers.</button></li>
                        <li><button>How do the employees rank in terms of sales performance?</button></li>
                        <li><button>Which 5 cities have the most customers?</button></li>
                    </ul>
                </section>

                <!-- 输入区域 -->
                <section id="inputSection">
                    <input type="text" id="userInput" placeholder="Ask me a question about your data that I can turn into SQL.">
                    <button id="submitQuestion">Submit</button>
                </section>
            </header>

            <!--侧边栏选择的内容页面-->
            <section id="contentArea">
                <!-- Content will be loaded here based on the sidebar selection -->
                <!--Function页面内容-->
                <h1>Functions</h1>
                <p>No functions found</p>
                <div id="newFunctionBox" class="function-box">
                    <h3>New</h3>
                    <p>Create a new function</p>
                    <button id="createButton">Create ></button>
                </div>

                <!--训练数据页面内容-->
                <section id="trainingDataPage" class="training-data-page">
                    <h1>Add Training Data</h1>
                    <div id="trainingDataBox" class="training-box">
                        <p>Training Data Type</p>
                        <button id="DDLButton">DDL</button>
                        <button id="DocumenButton">Documentation</button>
                        <button id="SQLButton">SQL</button>
                        <button id="QuestionButton">Question</button>
                    </div>

                    <p>Your SQL</p>
                    <div id="inputBox" class="input-box">

                    </div>
            </section>
        </div>
    </div>
    <footer>
        <p>&copy; 2024 Jenasi.AI. All rights reserved.</p>
    </footer>
    <script src="/assets/index-35bab439.js"></script>
</body>
</html>
'''

css_content = '''
/* 基础样式 */
body, html {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
}

/*布局样式*/
.layout{
    display: flex;
    height: 100vh;
    width: 100%;
}

/* 侧边栏样式 */
.sidebar {
    width: 20%; /* 调整为页面宽度的五分之一 */
    background-color: #f4f4f4;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    /* 添加分割线效果 */
}

/*侧边栏logo*/
.sidebar-logo {
    width: 40px;
    height: 40px;
    margin-bottom: 10px; /*添加下边距，和标题保持间隔*/
    vertical-align: middle;
}

.sidebar h2 {
    margin: 0 0 20px;
    font-size: 1.5em;
    display: inline-block;
    vertical-align: middle;
}

.sidebar button {
    width: 100%;
    padding: 10px;
    text-align: center;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.sidebar button:hover {
    background-color: #eee;
}

.sidebar ul {
    list-style-type: none;
    padding: 0;
    width: 100%;
}

.sidebar ul li {
    margin-bottom: 10px;
}

#signout{
    margin-bottom: auto;
    /*让按钮固定在侧边栏底部*/
}

/* 主内容区域样式 */
.main-content {
    display: flex;
    justify-content: center;
    align-items: center; /*水平居中*/
    flex-grow: 1;
    flex-direction: column; /*从上到下的布局*/
    height: 100%; /*沾满视觉高度*/
    width: 80%;
    padding-top: 10vh;
    margin-left: 0
    text-align: center;
    overflow-y: auto; /* 如果内容过长，可滚动 */
    background-color: #fff; /* 设置白色背景 */
}

header {
    display: flex;
    flex-direction: column;
    justify-content: center; /*垂直居中*/
    align-items: center; /*水平居中*/
    height: 100%;
    text-align: center; /*保证文字水平居中*/
    margin-bottom: 20px;
    <link rel="stylesheet" href="style.css">
}

h1{
    margin:0;
    font-weight: 2.5em;
    color: #333;
}

p{
    font-size: 1.2em;
    color: #666;
}

#contentArea {
    min-height: 300px; /* 确保内容区域有最小高度 */
    width: 80%;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100vh;
    padding-top: 10vh;
    text-align: center;
    font-size: 1.2em;
}

/* 底部样式 */
footer {
    background-color: #f2f2f2;
    text-align: center;
    padding: 10px;
    width: 100%;
    position: fixed;
    bottom: 0;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1); /* 添加顶部阴影 */
}

/*Function页面框样式*/
.function-box {
    border: 1px solid #ddd; /*边框*/
    border-radius: 5px; /*圆角*/
    padding: 20px; /*内边距*/
    margin:20px auto; /*居中*/
    width: 300px; /*固定宽度*/
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /*阴影*/
    background-color: #f9f9f9; /*背景色*/
}

.function-box h3 {
    margin: 0;
    font-size: 1.5em;
    color: #333;
}

.function-box p {
    font-size: 1em;
    color: #666;
    margin: 10px 0 20px;
}

.function-box button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #007BFF;
    color: #fff;
    font-size: 1em;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.function-box button:hover {
    background-color: #0056b3;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .sidebar {
        width: 100%; /* 在小屏幕上全宽显示 */
    }

    .layout{
        flex-direction: column;
        /* 小屏幕上侧边栏和内容垂直排列 */
    }

    .main-content {
        margin-left: 0; /* 移除左边距 */
    }
}

/*问题列表样式*/
#exampleQuestions {
    margin-top: 20px; /* 与标题保持间距 */
    text-align: center; /* 居中对齐 */
}

#exampleQuestions h3 {
    font-size: 1.2em;
    color: #333;
}

#exampleQuestions ul {
    list-style-type: none; /* 移除默认列表样式 */
    padding: 0;
}

#exampleQuestions ul li {
    margin: 10px 0; /* 每个问题按钮的间距 */
}

#exampleQuestions ul li button {
    padding: 10px 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    cursor: pointer;
    background-color: #fff;
    transition: background-color 0.2s ease;
}

#exampleQuestions ul li button:hover {
    background-color: #f4f4f4;
}

/*训练数据页面样式设计*/
.training-data-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.training-data-page h1 {
    font-size: 2em;
    color: #333;
    margin-bottom: 20px;
}

.button-options {
    display: flex;
    flex-direction: column;
    gap:10px;
    margin-bottom: 20px;
}

.button-options button {
    padding: 10px;
    width: 200px;
    font-size: 1.2em;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.button-options button:hover {
    background-color: #0056b3;
}

#inputBox {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap:15px;
    padding: 20px;
}

.input-box {
    display: flex;
    flex-direction: column;
    gap:10px;
}

.input-box input {
    padding: 10px;
    font-size: 1em;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 300%;
}

.input-box label {
    font-size: 1.2em;
    color: #333;
}

'''

js_content = '''
document.addEventListener('DOMContentLoaded', function() {
    // 获取按钮元素
    const functionsButton = document.getElementById('functionsButton');
    const trainingDataButton = document.getElementById('trainingDataButton');
    const newQuestionButton = document.getElementById('newQuestion');
    const createButton = document.getElementById('createButton');

    const DDLButton = document.getElementById('DDLButton');
    const DocumenButton = document.getElementById('DocumenButton');
    const SQLButton = document.getElementById('SQLButton');
    const QuestionButton=document.getElementById('QuestionButton');

    const inputBox=document.getElementById('inputBox');

    //初始化，显示主页面内容
    toggleView('welcome');

    // 为每个按钮添加点击事件
    functionsButton.addEventListener('click', function() {
    toggleView('functions');
    });

    trainingDataButton.addEventListener('click', function() {
        toggleView('training-data');
    });

    newQuestionButton.addEventListener('click', function() {
        toggleView('welcome'); // 调用主页面显示逻辑
    });

    createButton.addEventListener('click', function() {
        toggleView('welcome'); //调用主页面显示逻辑
    });

    function toggleView(viewId) {
        const header = document.querySelector('header'); // 主页面内容
        const contentArea = document.getElementById('contentArea'); // 功能页面内容

        header.style.display = 'none';
        contentArea.style.display = 'none';

        if (viewId === 'welcome') {
        // 显示主页面内容
        header.style.display = 'block';
        contentArea.innerHTML = `
            <section id="inputSection">
                <input type="text" id="userInput" placeholder="Ask me a question about your data that I can turn into SQL.">
                <button id="submitQuestion">Submit</button>
            </section>
        `;
        } else if (viewId === 'functions') {
            fetchFunctionsData(); // 加载功能页面
            contentArea.style.display = 'block';
        } else if (viewId === 'training-data') {
            fetchTrainingData(); // 加载训练数据页面
            contentArea.style.display = 'block';
        }
}

    function fetchFunctionsData() {
        const contentArea = document.getElementById('contentArea');
        contentArea.innerHTML=`
            <h2>Functions</h2>
            <p>No functions found</p>
            <div id="newFunctionBox" class="function-box">
                <h3>New</h3>
                <p>Create a new function</p>
                <button id="createButton">Create ></button>
            </div>
        `;

        //绑定按钮点击事件
        const createButton = document.getElementById('createButton');
        createButton.addEventListener('click', function() {
            toggleView('welcome');
        });
        fetch('/api/functions')
            .then((response) => response.json())
            .then((data) => {
                contentArea.innerHTML = `<h2>Functions Page</h2><p>${data.description}</p>`;
            })
            .catch((error) => console.error('Error fetching functions data:', error));
    }

    function fetchTrainingData() {
        const contentArea = document.getElementById('contentArea');
        contentArea.innerHTML = `
            <h2>Training Data</h2>
            <p>Choose the type of training data your want to add.</p>
        `
        fetch('/api/training-data')
            .then((response) => response.json())
            .then((data) => {
                contentArea.innerHTML = `<h2>Training Data Page</h2><p>${data.description}</p>`;
            })
            .catch((error) => console.error('Error fetching training data:', error));
    }
});

'''
