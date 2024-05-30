import { useState } from "react";
import './App.css';

function Header({ onChangeMode, children }) {
  return (
    <header>
      <h1 onClick={() => onChangeMode()}>{children}</h1>
      <p className="subtitle">먹었을 때 든든한 고봉밥처럼, 오늘 하루 당신의 일정이 고봉밥처럼 든든하길 바랍니다.</p>
    </header>
  );
}

function Nav({ onChangeMode, list }) {
  return (
    <nav>
      <ol>
        {list.map((item) => (
          <li key={item.id} onClick={() => onChangeMode(item.id)}>
            <div>{item.title}</div>
          </li>
        ))}
      </ol>
    </nav>
  );
}

function Article(props) {
  return (
    <article>
      <h2>{props.title}</h2>
      <p>{props.content}</p>
    </article>
  );
}

function Create({ onCreate }) {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const handleClick = () => {
    onCreate(title, content);
    setTitle("");
    setContent("");
  };

  return (
    <div>
      <p>
        <input type="text" placeholder="title" value={title} onChange={(e) => setTitle(e.target.value)} />
      </p>
      <p>
        <textarea placeholder="content" value={content} onChange={(e) => setContent(e.target.value)}></textarea>
      </p>
      <p>
        <button type="button" onClick={handleClick}>생성</button>
      </p>
    </div>
  );
}

function Update({ onUpdate, item }) {
  const [title, setTitle] = useState(item.title);
  const [content, setContent] = useState(item.content);

  const handleClick = () => {
    onUpdate(title, content);
  };

  return (
    <div>
      <p>
        <input
          type="text"
          placeholder="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </p>
      <p>
        <textarea
          placeholder="content"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        ></textarea>
      </p>
      <p>
        <button type ="button" onClick={handleClick}>수정</button>
      </p>
    </div>
  );
}

function App() {
  const [mode, setMode] = useState("HOME");
  const [id, setId] = useState(-1);
  const [list, setList] = useState([
    { id: 0, title: "수업 듣기", content: "2교시 심리철학" },
    { id: 1, title: "점심 약속", content: "13시 어흥 식당" },
    { id: 2, title: "넥스트 세션", content: "19시 반 스타트업 스테이션" },
  ]);

  let title;
  let content;

  if (mode === "HOME") {
    title = "인사";
    content = "안녕하세요. 조철종입니다.";
  } else if (mode === "READ") {
    title = list[id].title;
    content = list[id].content;
  }

  const handleCreate = (title, content) => {
    setList([...list, { title, content, id: list.length }]);
    setMode("HOME");
  };

  const handleUpdate = (title, content) => {
    setList(
      list.map((item) => (item.id === id ? { ...item, title, content } : item))
    );
    setMode("READ");
  };

  const handleDelete = () => {
    setList(list.filter((item) => item.id !== id));
    setMode("HOME");
    setId(-1);
  };

  return (
    <>
      <div className="wrapper">
        <Header onChangeMode={() => setMode("HOME")}>오늘의 할 일</Header>
        <div className="rice-bowl">
          <div className="rice-layer-top"></div>
          <Nav list={list} onChangeMode={(_id) => { setMode("READ"); setId(_id); }}></Nav>
        </div>
        <Article title={title} content={content}></Article>
      </div>
      {mode === "CREATE" && <Create onCreate={handleCreate} />}
      {mode === "HOME" && (
        <button onClick={() => setMode("CREATE")}>한 숟갈 더</button>
      )}
      {mode === "READ" && (
        <>
          <button onClick={() => setMode("UPDATE")}>수정</button>
          <button onClick={handleDelete}>덜어내기</button>
        </>
      )}
      {mode === "UPDATE" && (
        <Update
          onUpdate={handleUpdate}
          item={list.find((item) => item.id === id)}
        />
      )}
    </>
  );
}

export default App;