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
    :root {
        --primary-green: #2d5a27;
        --light-green: #3a7a33;
        --card-bg: #fff;
        --card-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        --border-radius: 12px;
        --text-main: #2d2d2d;
        --text-muted: #666;
    }

    .banner {
        background: linear-gradient(90deg, var(--primary-green), var(--light-green));
        color: #fff;
        border-radius: var(--border-radius);
        padding: 1.5rem 2rem;
        margin: 2rem auto 1.5rem auto;
        max-width: 700px;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 2px 8px rgba(45, 90, 39, 0.15);
    }
    .card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 700px;
    }
    .section-title {
        color: var(--primary-green);
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
        color: var(--text-main);
    }
    .event-date {
        color: var(--primary-green);
        font-weight: 600;
        margin-left: 0.5rem;
    }
    .messages-section {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
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
        color: var(--text-main);
    }
    .message-user {
        color: var(--primary-green);
        font-weight: 600;
        margin-right: 0.5em;
    }
    .message-input {
        width: 80%;
        padding: 0.5rem 1rem;
        border-radius: var(--border-radius);
        border: 1px solid rgba(45, 90, 39, 0.2);
        font-size: 1rem;
        margin-right: 0.5rem;
    }
    .send-btn {
        background: linear-gradient(90deg, var(--primary-green), var(--light-green));
        color: #fff;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.5rem 1.2rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }
    .send-btn:hover {
        background: linear-gradient(90deg, var(--light-green), var(--primary-green));
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(45, 90, 39, 0.2);
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