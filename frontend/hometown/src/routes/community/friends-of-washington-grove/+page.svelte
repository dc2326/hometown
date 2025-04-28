<script>
    let messages = [
        { user: 'Maya', text: 'Looking forward to the next cleanup!' },
        { user: 'Chris', text: 'Can we bring snacks for volunteers?' }
    ];
    let newMessage = '';
    function sendMessage() {
        if (newMessage.trim()) {
            messages = [...messages, { user: 'You', text: newMessage }];
            newMessage = '';
        }
    }
    let events = [
        { name: 'Spring Cleanup', date: 'Sat, May 18', time: '9:00am' },
        { name: 'Trail Maintenance', date: 'Sat, May 25', time: '10:00am' },
        { name: 'Picnic & Planning', date: 'Sun, June 2', time: '12:00pm' }
    ];
</script>

<style>
    .banner {
        background: linear-gradient(90deg, #2d2dff, #7c3aed);
        color: #fff;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 2rem auto 1.5rem auto;
        max-width: 700px;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
    }
    .card {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 700px;
    }
    .section-title {
        color: #2d2dff;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .event-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .event-item {
        margin-bottom: 0.75rem;
        color: #22223b;
    }
    .event-date {
        color: #7c3aed;
        font-weight: 600;
        margin-left: 0.5rem;
    }
    .messages-section {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 700px;
    }
    .message-list {
        max-height: 180px;
        overflow-y: auto;
        margin-bottom: 1rem;
    }
    .message-item {
        margin-bottom: 0.75rem;
        color: #22223b;
    }
    .message-user {
        color: #2d2dff;
        font-weight: 600;
        margin-right: 0.5em;
    }
    .message-input {
        width: 80%;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: 1px solid #d1d5db;
        font-size: 1rem;
        margin-right: 0.5rem;
    }
    .send-btn {
        background: linear-gradient(90deg, #2d2dff, #7c3aed);
        color: #fff;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: background 0.2s;
    }
    .send-btn:hover {
        background: linear-gradient(90deg, #7c3aed, #2d2dff);
    }
</style>

<div class="banner">Friends of Washington Grove</div>

<div class="messages-section">
    <div class="section-title">Messages</div>
    <div class="message-list">
        {#each messages as m}
            <div class="message-item"><span class="message-user">{m.user}:</span> {m.text}</div>
        {/each}
    </div>
    <input class="message-input" type="text" placeholder="Type a message..." bind:value={newMessage} on:keydown={(e) => e.key === 'Enter' && sendMessage()} />
    <button class="send-btn" on:click={sendMessage}>Send</button>
</div>

<div class="card">
    <div class="section-title">Upcoming Events</div>
    <ul class="event-list">
        {#each events as e}
            <li class="event-item">{e.name} <span class="event-date">({e.date}, {e.time})</span></li>
        {/each}
    </ul>
</div> 