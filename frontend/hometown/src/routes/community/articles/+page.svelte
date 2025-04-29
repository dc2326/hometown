<script>
    let articles = [
        {
            id: 1,
            title: 'Community Garden Project Takes Root',
            author: 'Sarah Johnson',
            date: 'May 1, 2024',
            excerpt: 'The new community garden initiative has officially launched, bringing together neighbors to grow fresh produce and build connections.',
            content: `The community garden project, which began as a small idea during last year's neighborhood meeting, has now blossomed into a thriving initiative. Located at the corner of Maple and Oak streets, the garden features 20 raised beds, a composting area, and a small greenhouse.

            "We've seen incredible enthusiasm from the community," says project coordinator Sarah Johnson. "Over 50 families have signed up to maintain plots, and we've already harvested our first batch of vegetables."

            The garden not only provides fresh produce but also serves as an educational space for local schools and a gathering place for neighbors. Weekly workshops on sustainable gardening practices are held every Saturday morning.

            Future plans include expanding the garden to include a children's learning area and installing a rainwater collection system. The project has received support from local businesses and the city council, with plans to replicate the model in other neighborhoods.`,
            image: '/garden.jpg'
        },
        {
            id: 2,
            title: 'Annual Spring Festival Draws Record Crowd',
            author: 'Michael Chen',
            date: 'April 28, 2024',
            excerpt: 'This year\'s Spring Festival broke attendance records with over 5,000 visitors enjoying local food, music, and crafts.',
            content: `The 15th Annual Spring Festival was a resounding success, drawing visitors from across the region to celebrate the season. Held in Washington Grove Park, the event featured over 100 local vendors, three stages of live music, and activities for all ages.

            "The energy this year was incredible," said festival organizer Michael Chen. "We saw a 30% increase in attendance compared to last year, and the feedback has been overwhelmingly positive."

            Highlights included:
            - A farmers' market showcasing local produce
            - Live performances from 20 local bands
            - Children's activities including face painting and crafts
            - Food trucks offering diverse cuisines
            - Artisan market with handmade goods

            The festival also raised over $10,000 for local schools through ticket sales and donations. Plans are already underway for next year's event, with organizers promising even more attractions and activities.`,
            image: '/festival.jpg'
        },
        {
            id: 3,
            title: 'New Community Center Opens Its Doors',
            author: 'Lisa Rodriguez',
            date: 'April 25, 2024',
            excerpt: 'The long-awaited community center officially opened this week, offering a variety of programs and services for residents of all ages.',
            content: `After years of planning and construction, the new Maplewood Community Center has finally opened its doors to the public. The state-of-the-art facility features a gymnasium, computer lab, art studio, and multipurpose rooms for community events.

            "This is a dream come true for our community," said Mayor James Wilson at the ribbon-cutting ceremony. "The center will serve as a hub for learning, recreation, and social connection."

            Initial programs include:
            - After-school tutoring and homework help
            - Senior fitness classes
            - Art and music workshops
            - Community meetings and events
            - Technology training for all ages

            The center is open seven days a week and offers both free and low-cost programs. Membership options are available for those who want to take advantage of all the facilities.`,
            image: '/center.jpg'
        },
        {
            id: 4,
            title: 'Local Students Win Science Fair',
            author: 'David Thompson',
            date: 'April 22, 2024',
            excerpt: 'Students from Central High School took home top prizes at the regional science fair, showcasing innovative projects in renewable energy and environmental science.',
            content: `Central High School's science team made history this weekend by winning first place in three categories at the Regional Science Fair. Their projects focused on sustainable solutions to local environmental challenges.

            The winning projects included:
            - A solar-powered water filtration system
            - A study on urban bee populations
            - An innovative composting method for apartment dwellers

            "These students have shown incredible dedication and creativity," said science teacher Dr. Emily Chen. "Their work has real-world applications and could make a significant impact on our community."

            The team will now advance to the state competition next month, where they hope to secure funding to implement their projects in the community.`,
            image: '/science.jpg'
        }
    ];

    let selectedArticle = null;
    let showModal = false;

    function openArticle(article) {
        selectedArticle = article;
        showModal = true;
    }

    function closeModal() {
        showModal = false;
        selectedArticle = null;
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

    .articles-container {
        max-width: 1200px;
        margin: 2rem auto;
        padding: 0 1rem;
    }

    .articles-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
    }

    .article-card {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        overflow: hidden;
        cursor: pointer;
        transition: all 0.3s;
        border: 1px solid rgba(45, 90, 39, 0.1);
    }

    .article-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(45, 90, 39, 0.15);
    }

    .article-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }

    .article-content {
        padding: 1.5rem;
    }

    .article-title {
        color: var(--primary-green);
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }

    .article-meta {
        color: var(--text-muted);
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }

    .article-excerpt {
        color: var(--text-main);
        line-height: 1.6;
    }

    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }

    .modal {
        background: var(--card-bg);
        border-radius: var(--border-radius);
        box-shadow: var(--card-shadow);
        max-width: 800px;
        width: 90%;
        max-height: 90vh;
        overflow-y: auto;
        position: relative;
    }

    .modal-close {
        position: absolute;
        top: 1rem;
        right: 1rem;
        background: var(--primary-green);
        color: #fff;
        border: none;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        font-size: 1.2rem;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s;
    }

    .modal-close:hover {
        background: var(--light-green);
        transform: rotate(90deg);
    }

    .modal-image {
        width: 100%;
        height: 300px;
        object-fit: cover;
    }

    .modal-content {
        padding: 2rem;
    }

    .modal-title {
        color: var(--primary-green);
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }

    .modal-meta {
        color: var(--text-muted);
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    .modal-text {
        color: var(--text-main);
        line-height: 1.8;
        white-space: pre-line;
    }
</style>

<div class="articles-container">
    <div class="articles-grid">
        {#each articles as article}
            <div class="article-card" on:click={() => openArticle(article)}>
                <img class="article-image" src={article.image} alt={article.title} />
                <div class="article-content">
                    <h2 class="article-title">{article.title}</h2>
                    <div class="article-meta">By {article.author} | {article.date}</div>
                    <div class="article-excerpt">{article.excerpt}</div>
                </div>
            </div>
        {/each}
    </div>
</div>

{#if showModal && selectedArticle}
    <div class="modal-overlay" on:click={closeModal}>
        <div class="modal" on:click|stopPropagation>
            <button class="modal-close" on:click={closeModal}>×</button>
            <img class="modal-image" src={selectedArticle.image} alt={selectedArticle.title} />
            <div class="modal-content">
                <h1 class="modal-title">{selectedArticle.title}</h1>
                <div class="modal-meta">By {selectedArticle.author} | {selectedArticle.date}</div>
                <div class="modal-text">{selectedArticle.content}</div>
            </div>
        </div>
    </div>
{/if} 