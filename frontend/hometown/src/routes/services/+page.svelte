<script>
    let services = [
        {
            title: 'Pay Taxes',
            description: 'File and pay property taxes, business taxes, and view payment history',
            icon: '💰',
            contact: 'taxes@hometown.gov',
            hours: '24/7 Online',
            link: '/services/taxes'
        },
        {
            title: 'File Permits',
            description: 'Apply for building permits, business licenses, and special event permits',
            icon: '📝',
            contact: 'permits@hometown.gov',
            hours: 'Mon-Fri: 9am-4pm',
            link: '/services/permits'
        },
        {
            title: 'Utilities',
            description: 'Pay bills, track usage, and manage your utility accounts',
            icon: '💧',
            contact: 'utilities@hometown.gov',
            hours: '24/7 Online',
            link: '/services/utilities'
        },
        {
            title: 'Fines & Tickets',
            description: 'Pay parking tickets, court fines, and other violations',
            icon: '🚗',
            contact: 'fines@hometown.gov',
            hours: '24/7 Online',
            link: '/services/fines'
        },
        {
            title: 'Voting',
            description: 'Register to vote, request a ballot, and find polling locations',
            icon: '🗳️',
            contact: 'elections@hometown.gov',
            hours: '24/7 Online',
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
    }

    .services-container {
        max-width: 1200px;
        margin: 2rem auto;
        padding: 0 1rem;
        background: var(--background);
        min-height: 100vh;
    }

    .page-title {
        color: var(--primary-green);
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        padding-bottom: 1rem;
    }

    .page-title::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 4px;
        background: var(--primary-brown);
    }

    .services-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    .service-card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        padding: 2rem;
        transition: transform 0.3s, box-shadow 0.3s;
        cursor: pointer;
        border: 1px solid rgba(139, 69, 19, 0.1);
        position: relative;
        overflow: hidden;
    }

    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: var(--primary-green);
    }

    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(43, 43, 43, 0.15);
    }

    .service-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        color: var(--primary-brown);
    }

    .service-title {
        color: var(--primary-green);
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .service-description {
        color: var(--text-muted);
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }

    .service-details {
        border-top: 1px solid rgba(139, 69, 19, 0.1);
        padding-top: 1rem;
        margin-top: 1rem;
    }

    .service-contact {
        color: var(--primary-brown);
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .service-hours {
        color: var(--text-muted);
        font-size: 0.9rem;
    }

    @media (max-width: 768px) {
        .services-grid {
            grid-template-columns: 1fr;
        }
    }
</style>

<div class="services-container">
    <h1 class="page-title">Town Services</h1>
    <div class="services-grid">
        {#each services as service}
            <div class="service-card" on:click={() => handleClick(service.link)}>
                <div class="service-icon">{service.icon}</div>
                <h2 class="service-title">{service.title}</h2>
                <p class="service-description">{service.description}</p>
                <div class="service-details">
                    <div class="service-contact">{service.contact}</div>
                    <div class="service-hours">{service.hours}</div>
                </div>
            </div>
        {/each}
    </div>
</div> 