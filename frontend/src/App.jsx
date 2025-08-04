import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; 

function App() {
  const [text, setText] = useState('');
  const [sourceLang, setSourceLang] = useState('en');
  const [targetLang, setTargetLang] = useState('ko');
  const [result, setResult] = useState('');

  const handleTranslate = async () => {
    const res = await axios.post('http://localhost:8000/translate', {
      text,
      source_lang: sourceLang,
      target_lang: targetLang,
    });
    setResult(res.data.translated_text);
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>웹 번역기</h1>
      <textarea value={text} onChange={e => setText(e.target.value)} rows={5} cols={50} />
      <br />
      <select value={sourceLang} onChange={e => setSourceLang(e.target.value)}>
        <option value="en">영어</option>
        <option value="ko">한국어</option>
        <option value="ja">일본어</option>
      </select>
      →
      <select value={targetLang} onChange={e => setTargetLang(e.target.value)}>
        <option value="ko">한국어</option>
        <option value="en">영어</option>
        <option value="ja">일본어</option>
      </select>
      <br /><br />
      <button onClick={handleTranslate}>번역</button>
      <h3>결과:</h3>
      <p>{result}</p>
    </div>
  );
}

export default App;