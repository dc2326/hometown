<script>
    // Example events from all communities
    let calendarEvents = [
        {
            title: 'Book Club: Next Meeting',
            community: 'Book Club',
            start: '2025-04-28T19:00',
            end: '2025-04-28T21:00',
            location: '123 Maple Ave',
            color: '#7c3aed'
        },
        {
            title: 'Little League Practice',
            community: 'Little League Baseball',
            start: '2025-04-29T16:00',
            end: '2025-04-29T18:00',
            location: 'Main Field',
            color: '#2d2dff'
        },
        {
            title: 'Little League Game',
            community: 'Little League Baseball',
            start: '2025-05-01T17:30',
            end: '2025-05-01T19:00',
            location: 'Field 2',
            color: '#2d2dff'
        },
        {
            title: 'Rides to School: Signup',
            community: 'Rides to School',
            start: '2025-04-30T07:30',
            end: '2025-04-30T08:00',
            location: 'Maple Grove',
            color: '#00bcd4'
        },
        {
            title: 'Blessed Sacrament Church: Service',
            community: 'Blessed Sacrament Church',
            start: '2025-05-04T10:30',
            end: '2025-05-04T12:00',
            location: '456 Church St',
            color: '#ff9800'
        },
        {
            title: 'Friends of Washington Grove: Cleanup',
            community: 'Friends of Washington Grove',
            start: '2025-05-03T09:00',
            end: '2025-05-03T11:00',
            location: 'Washington Grove Park',
            color: '#43a047'
        }
    ];

    // Calendar display helpers
    let weekStart = new Date('2025-04-27');
    let daysOfWeek = Array.from({length: 7}, (_, i) => {
        let d = new Date(weekStart);
        d.setDate(d.getDate() + i);
        return d;
    });
    function getEventsForDay(date) {
        return calendarEvents.filter(e => {
            let eventDate = new Date(e.start);
            return eventDate.toDateString() === date.toDateString();
        });
    }
    function formatTime(dt) {
        let d = new Date(dt);
        let h = d.getHours();
        let m = d.getMinutes();
        let ampm = h >= 12 ? 'pm' : 'am';
        h = h % 12;
        if (h === 0) h = 12;
        return `${h}:${m.toString().padStart(2, '0')}${ampm}`;
    }

    // Updated bulletin board messages to match communities
    let bulletinMessages = [
        {
            title: 'Book Club: Next Meeting',
            text: 'Do not forget! Book Club meets Friday at 7pm at 123 Maple Ave. Vote for next months book online.'
        },
        {
            title: 'Little League: Practice',
            text: 'Practice is Tuesday at 4pm, Main Field. Bring your glove and water!'
        },
        {
            title: 'Rides to School',
            text: 'New ride slots open for Maple Grove and Oak Hill. Sign up on the Rides page.'
        },
        {
            title: 'Friends of Washington Grove',
            text: 'Spring Cleanup this Saturday, 9am at the park. All volunteers welcome!'
        },
        {
            title: 'Blessed Sacrament Church',
            text: 'Sunday service at 10:30am. Youth Group meets Wednesday at 6pm.'
        }
    ];
    let publicNotices = [
        {
            title: 'Town Hall Meeting',
            date: 'May 10th, 6pm',
            location: 'Community Center',
            description: 'Discuss upcoming projects and community questions.'
        },
        {
            title: 'Spring Festival',
            date: 'May 15th',
            location: 'Main Street',
            description: 'Live music, food trucks, and games for all ages!'
        },
        {
            title: 'Water Service Maintenance',
            date: 'May 12th, 2-4pm',
            location: 'Townwide',
            description: 'Temporary water shutoff for scheduled maintenance.'
        }
    ];

    let featuredNews = [
        {
            title: 'Town Hall Meeting',
            date: 'May 15, 2024',
            excerpt: 'Join us for the monthly town hall meeting to discuss community initiatives.',
            image: '/park.jpg',
            link: '/news/town-hall-meeting'
        },
        {
            title: 'Spring Festival',
            date: 'May 5, 2024',
            excerpt: 'Annual Spring Festival brought together hundreds of community members.',
            image: '/field.jpg',
            link: '/news/spring-festival'
        }
    ];

    let quickLinks = [
        {
            title: 'Pay Taxes',
            icon: '💰',
            link: '/services/taxes'
        },
        {
            title: 'File Permits',
            icon: '📝',
            link: '/services/permits'
        },
        {
            title: 'Utilities',
            icon: '💧',
            link: '/services/utilities'
        },
        {
            title: 'Voting',
            icon: '🗳️',
            link: '/services/voting'
        }
    ];

    function handleClick(link) {
        window.location.href = link;
    }
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --primary-brown: #8b4513;
        --accent-gold: #d4af37;
        --background: #f5f5f0;
        --card-bg: #fff;
        --card-shadow: 0 4px 12px rgba(43, 43, 43, 0.1);
        --border-radius: 12px;
        --text-main: #2d2d2d;
        --text-muted: #666;
        --cork: #e2b07a;
        --pin-red: #e74c3c;
        --pin-blue: #3498db;
        --pin-green: #43a047;
        --calendar-green-1: #2d5a27;
        --calendar-green-2: #3d6a37;
        --calendar-green-3: #4d7a47;
        --calendar-green-4: #5d8a57;
        --calendar-green-5: #6d9a67;
        --calendar-green-6: #7daa77;
    }

    body, .background {
        background: var(--background);
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
        color: var(--text-main);
    }

    .main-container {
        display: flex;
        gap: 2rem;
        margin: 2rem auto;
        max-width: 1200px;
        min-height: 70vh;
    }

    .card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem 1.5rem;
        margin-bottom: 2rem;
    }

    .bulletin {
        flex: 2;
        margin-right: 1rem;
    }
    .public-notices {
        flex: 1;
        min-width: 320px;
    }

    .section-title {
        color: var(--primary-green);
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .notice-list, .personal-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .notice-list li, .personal-list li {
        padding: 0.75rem 0;
        border-bottom: 1px solid #ececec;
        color: var(--text-muted);
    }
    .notice-list li:last-child, .personal-list li:last-child {
        border-bottom: none;
    }
    .banner {
        background: var(--primary-green);
        color: #fff;
        border-radius: var(--border-radius);
        padding: 1rem 2rem;
        margin: 2rem auto 1.5rem auto;
        max-width: 1200px;
        font-size: 1.1rem;
        font-weight: 500;
        box-shadow: var(--card-shadow);
    }
    .calendar-section {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 8px rgba(44, 62, 80, 0.08);
        padding: 2rem;
        margin: 2rem auto;
        max-width: 1200px;
    }
    .calendar-title {
        color: var(--primary-green);
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    .calendar-table {
        width: 100%;
        border-collapse: collapse;
        table-layout: fixed;
    }
    .calendar-table th, .calendar-table td {
        border: 1px solid #ececec;
        padding: 0.5rem;
        vertical-align: top;
        min-height: 120px;
        height: 120px;
        background: #f5f6fa;
    }
    .calendar-table th {
        background: #f0f4ff;
        color: var(--primary-green);
        font-size: 1.1rem;
        font-weight: 600;
        text-align: center;
    }
    .calendar-event {
        margin-bottom: 0.5rem;
        border-radius: 8px;
        padding: 0.3rem 0.7rem;
        color: #fff;
        font-size: 0.98rem;
        font-weight: 500;
        box-shadow: 0 1px 4px rgba(44,62,80,0.08);
        display: block;
        background: var(--primary-green);
    }
    .calendar-event:nth-child(1) { background: var(--calendar-green-1); }
    .calendar-event:nth-child(2) { background: var(--calendar-green-2); }
    .calendar-event:nth-child(3) { background: var(--calendar-green-3); }
    .calendar-event:nth-child(4) { background: var(--calendar-green-4); }
    .calendar-event:nth-child(5) { background: var(--calendar-green-5); }
    .calendar-event:nth-child(6) { background: var(--calendar-green-6); }
    .calendar-event .event-title {
        font-weight: 700;
    }
    .calendar-event .event-time {
        font-size: 0.92em;
        opacity: 0.9;
    }
    .calendar-event .event-location {
        font-size: 0.9em;
        opacity: 0.8;
    }

    .bulletin-board {
        background: repeating-linear-gradient(135deg, var(--cork), #e7c18a 20px, var(--cork) 40px);
        border-radius: 18px;
        box-shadow: 0 4px 16px rgba(44,62,80,0.10);
        padding: 2.5rem 2rem 2rem 2rem;
        margin-bottom: 2rem;
        position: relative;
        min-height: 320px;
        display: flex;
        flex-direction: column;
        gap: 1.2rem;
    }
    .bulletin-title {
        font-size: 2rem;
        font-weight: 800;
        color: var(--primary-green);
        margin-bottom: 1.2rem;
        letter-spacing: 0.01em;
        text-shadow: 0 2px 8px rgba(44,62,80,0.08);
    }
    .note {
        background: #fffbe6;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(44,62,80,0.10);
        padding: 1.1rem 1.5rem 1.1rem 2.2rem;
        margin-bottom: 0.5rem;
        position: relative;
        min-width: 220px;
        max-width: 600px;
        font-size: 1.08rem;
        font-family: 'Segoe UI', Arial, sans-serif;
        border-left: 6px solid var(--primary-green);
    }
    .note .note-title {
        font-weight: 700;
        color: var(--primary-green);
        margin-bottom: 0.2rem;
        font-size: 1.13rem;
    }
    .note-pin {
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: var(--pin-red);
        position: absolute;
        left: 10px;
        top: 16px;
        box-shadow: 0 2px 6px rgba(44,62,80,0.12);
        border: 2px solid #fff;
    }
    .note:nth-child(2) .note-pin { background: var(--pin-blue); }
    .note:nth-child(3) .note-pin { background: var(--pin-green); }
    .note:nth-child(4) .note-pin { background: #fbc02d; }
    .note:nth-child(5) .note-pin { background: #8e44ad; }

    .public-notices {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
    }
    .public-card {
        background: linear-gradient(90deg, #f0f4ff 60%, #e7e7fa 100%);
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(44,62,80,0.10);
        padding: 1.5rem 2rem;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        border-left: 8px solid var(--primary-green);
        position: relative;
        min-width: 260px;
    }
    .public-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--primary-green);
        margin-bottom: 0.2rem;
    }
    .public-date {
        color: var(--primary-brown);
        font-weight: 600;
        font-size: 1.05rem;
    }
    .public-location {
        color: var(--primary-green);
        font-size: 1.02rem;
        font-weight: 500;
    }
    .public-desc {
        color: #444;
        font-size: 1.01rem;
    }

    .welcome-banner {
        background: linear-gradient(rgba(45, 90, 39, 0.9), rgba(45, 90, 39, 0.9)), url('/park.jpg');
        background-size: cover;
        background-position: center;
        color: white;
        padding: 4rem 2rem;
        border-radius: var(--border-radius);
        text-align: center;
        margin: 2rem auto;
        position: relative;
        overflow: hidden;
        max-width: 1200px;
    }

    .welcome-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .welcome-subtitle {
        font-size: 1.5rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }

    .welcome-button {
        background: var(--accent-gold);
        color: var(--primary-green);
        border: none;
        border-radius: 30px;
        padding: 1rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s;
    }

    .welcome-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(43, 43, 43, 0.2);
    }
</style>

<div class="banner">
    <span>🔔 Welcome! Stay tuned for the latest updates from your communities and the town.</span>
</div>

<div class="main-container">
    <div class="bulletin-board bulletin">
        <div class="bulletin-title">Bulletin Board</div>
        {#each bulletinMessages as m, i}
            <div class="note">
                <div class="note-pin"></div>
                <div class="note-title">{m.title}</div>
                <div>{m.text}</div>
            </div>
        {/each}
    </div>
    <div class="public-notices public">
        <div class="section-title">Public Notices & Events</div>
        {#each publicNotices as n}
            <div class="public-card">
                <div class="public-title">{n.title}</div>
                <div class="public-date">{n.date}</div>
                <div class="public-location">{n.location}</div>
                <div class="public-desc">{n.description}</div>
            </div>
        {/each}
    </div>
</div>

<div class="calendar-section">
    <div class="calendar-title">Community Calendar</div>
    <table class="calendar-table">
        <thead>
            <tr>
                {#each daysOfWeek as d}
                    <th>{d.toLocaleDateString(undefined, { weekday: 'short', month: 'short', day: 'numeric' })}</th>
                {/each}
            </tr>
        </thead>
        <tbody>
            <tr>
                {#each daysOfWeek as d}
                    <td>
                        {#each getEventsForDay(d) as e}
                            <div class="calendar-event">
                                <div class="event-title">{e.title}</div>
                                <div class="event-time">{formatTime(e.start)} - {formatTime(e.end)}</div>
                                <div class="event-location">{e.location}</div>
                                <div style="font-size:0.85em;opacity:0.8;">{e.community}</div>
                            </div>
                        {/each}
                    </td>
                {/each}
            </tr>
        </tbody>
    </table>
</div>

<div class="welcome-banner">
    <h1 class="welcome-title">Welcome to Hometown</h1>
    <p class="welcome-subtitle">Your community, your home, your future</p>
    <button class="welcome-button" on:click={() => handleClick('/about')}>Learn More</button>
</div>