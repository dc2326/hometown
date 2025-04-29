<script>
    let riders = [
        { name: 'John D.', neighborhood: 'Maple Grove', grade: '11', school: 'Central High' },
        { name: 'Sarah P.', neighborhood: 'Oak Hill', grade: '10', school: 'Westview Academy' },
        { name: 'Emily S.', neighborhood: 'Maple Grove', grade: '9', school: 'Central High' },
        { name: 'Liam T.', neighborhood: 'Pine Estates', grade: '12', school: 'Central High' }
    ];
    let days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
    ];
    let slots = {
        Monday: ['7:30am - John D.', '7:45am - (open)'],
        Tuesday: ['7:30am - (open)', '7:45am - Sarah P.'],
        Wednesday: ['7:30am - John D.', '7:45am - (open)'],
        Thursday: ['7:30am - (open)', '7:45am - (open)'],
        Friday: ['7:30am - Sarah P.', '7:45am - (open)']
    };
    let messages = [
        { user: 'Sarah P.', text: 'Can anyone take my son on Thursday?' },
        { user: 'John D.', text: 'I can help on Wednesday!' }
    ];
    let newMessage = '';
    function sendMessage() {
        if (newMessage.trim()) {
            messages = [...messages, { user: 'You', text: newMessage }];
            newMessage = '';
        }
    }
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
        max-width: 900px;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 2px 8px rgba(45, 90, 39, 0.15);
    }

    .rider-table-card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 900px;
        border: 1px solid rgba(45, 90, 39, 0.1);
    }

    .rider-table {
        width: 100%;
        border-collapse: collapse;
    }

    .rider-table th, .rider-table td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid rgba(45, 90, 39, 0.1);
        text-align: left;
    }

    .rider-table th {
        color: var(--primary-green);
        font-size: 1.1rem;
        font-weight: 600;
    }

    .rider-table td {
        color: var(--text-main);
        font-size: 1rem;
    }

    .calendar {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 900px;
        border: 1px solid rgba(45, 90, 39, 0.1);
    }

    .calendar-table {
        width: 100%;
        border-collapse: collapse;
    }

    .calendar-table th, .calendar-table td {
        padding: 1rem;
        border-bottom: 1px solid rgba(45, 90, 39, 0.1);
        text-align: left;
    }

    .calendar-table th {
        color: var(--primary-green);
        font-size: 1.1rem;
        font-weight: 600;
    }

    .calendar-table td {
        color: var(--text-main);
        font-size: 1rem;
    }

    .messages-section {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 900px;
        border: 1px solid rgba(45, 90, 39, 0.1);
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
        transition: all 0.3s;
    }

    .message-input:focus {
        outline: none;
        border-color: var(--primary-green);
        box-shadow: 0 0 0 2px rgba(45, 90, 39, 0.1);
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

<div class="banner">Rides to School</div>

<div class="rider-table-card">
    <h2 style="color:var(--primary-green); margin-bottom:1rem;">Riders in this Group</h2>
    <table class="rider-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Neighborhood</th>
                <th>Grade</th>
                <th>School</th>
            </tr>
        </thead>
        <tbody>
            {#each riders as r}
                <tr>
                    <td>{r.name}</td>
                    <td>{r.neighborhood}</td>
                    <td>{r.grade}</td>
                    <td>{r.school}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<div class="calendar">
    <h2 style="color:var(--primary-green); margin-bottom:1rem;">Weekly Ride Signup</h2>
    <table class="calendar-table">
        <thead>
            <tr>
                <th>Day</th>
                <th>Slots</th>
            </tr>
        </thead>
        <tbody>
            {#each days as day}
                <tr>
                    <td>{day}</td>
                    <td>
                        {#each slots[day] as slot}
                            <div>{slot}</div>
                        {/each}
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<div class="messages-section">
    <h2 style="color:var(--primary-green); margin-bottom:1rem;">Messages</h2>
    <div class="message-list">
        {#each messages as m}
            <div class="message-item"><span class="message-user">{m.user}:</span> {m.text}</div>
        {/each}
    </div>
    <input class="message-input" type="text" placeholder="Type a message..." bind:value={newMessage} on:keydown={(e) => e.key === 'Enter' && sendMessage()} />
    <button class="send-btn" on:click={sendMessage}>Send</button>
</div> 