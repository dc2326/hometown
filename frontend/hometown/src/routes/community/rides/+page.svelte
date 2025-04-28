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
    .banner {
        background: linear-gradient(90deg, #7c3aed, #2d2dff);
        color: #fff;
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 2rem auto 1.5rem auto;
        max-width: 900px;
        font-size: 2rem;
        font-weight: 700;
        text-align: center;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
    }
    .rider-table-card {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 900px;
    }
    .rider-table {
        width: 100%;
        border-collapse: collapse;
    }
    .rider-table th, .rider-table td {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #ececec;
        text-align: left;
    }
    .rider-table th {
        color: #2d2dff;
        font-size: 1.1rem;
    }
    .rider-table td {
        color: #7c3aed;
        font-size: 1rem;
    }
    .calendar {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 900px;
    }
    .calendar-table {
        width: 100%;
        border-collapse: collapse;
    }
    .calendar-table th, .calendar-table td {
        padding: 1rem;
        border-bottom: 1px solid #ececec;
        text-align: left;
    }
    .calendar-table th {
        color: #7c3aed;
        font-size: 1.1rem;
    }
    .calendar-table td {
        color: #2d2dff;
        font-size: 1rem;
    }
    .messages-section {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin: 0 auto 2rem auto;
        max-width: 900px;
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
        color: #7c3aed;
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
        background: linear-gradient(90deg, #7c3aed, #2d2dff);
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
        background: linear-gradient(90deg, #2d2dff, #7c3aed);
    }
</style>

<div class="banner">Rides to School</div>

<div class="rider-table-card">
    <h2 style="color:#2d2dff; margin-bottom:1rem;">Riders in this Group</h2>
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
    <h2 style="color:#2d2dff; margin-bottom:1rem;">Weekly Ride Signup</h2>
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
    <h2 style="color:#7c3aed; margin-bottom:1rem;">Messages</h2>
    <div class="message-list">
        {#each messages as m}
            <div class="message-item"><span class="message-user">{m.user}:</span> {m.text}</div>
        {/each}
    </div>
    <input class="message-input" type="text" placeholder="Type a message..." bind:value={newMessage} on:keydown={(e) => e.key === 'Enter' && sendMessage()} />
    <button class="send-btn" on:click={sendMessage}>Send</button>
</div> 