import { useState } from 'react';

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    const text = input.trim();
    if (!text) return;
    setMessages(prev => [...prev, { role: 'user', content: text }]);
    setInput('');
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: 'demo', content: text })
      });
      const data = await res.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.response }]);
    } catch (err) {
      console.error(err);
      setMessages(prev => [...prev, { role: 'assistant', content: 'Error contacting the AI.' }]);
    }
  };

  return (
    <div style={{ padding: '1rem', maxWidth: '640px', margin: '0 auto' }}>
      <h1>SageSpark Core</h1>
      <div style={{ border: '1px solid #ccc', padding: '1rem', height: '300px', overflowY: 'auto', marginBottom: '1rem' }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ textAlign: msg.role === 'user' ? 'right' : 'left' }}>
            <strong>{msg.role === 'user' ? 'You' : 'SageSpark'}:</strong> {msg.content}
          </div>
        ))}
      </div>
      <div style={{ display: 'flex' }}>
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => {
            if (e.key === 'Enter') handleSend();
          }}
          style={{ flex: 1, padding: '0.5rem' }}
        />
        <button onClick={handleSend} style={{ padding: '0.5rem 1rem' }}>Send</button>
      </div>
    </div>
  );
}
