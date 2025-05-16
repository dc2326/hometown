<script>
    let article = {
        title: 'Robotics Team Wins State Championship',
        date: 'May 10, 2024',
        author: 'Michael Chen',
        readTime: '4 min read',
        image: '/robot.jpg',
        content: `
            The Hometown High Robotics Team, known as "The Innovators," brought home the state championship trophy after an intense three-day competition at the State Tech Expo. This marks the first time in school history that our robotics team has won the state title.

            The team's winning robot, named "Atlas," impressed judges with its innovative design and flawless execution of complex tasks. "What set Atlas apart was its unique approach to problem-solving," said competition judge Dr. Emily Rodriguez. "The team demonstrated exceptional creativity and technical skill."

            Team members spent over 500 hours designing, building, and programming Atlas. Their hard work paid off as they outperformed 32 other teams in a series of challenges that tested robot capabilities in navigation, object manipulation, and autonomous decision-making.

            "This victory is a testament to our students' dedication and the support of our community," said team advisor Mr. James Wilson. "The local tech companies that sponsored our team and the parents who volunteered their time made this achievement possible."

            The team's next challenge will be the National Robotics Championship in Chicago next month. The school is planning a community send-off event to wish them luck in their national competition.

            Team members include:
            • Sarah Martinez (Team Captain)
            • Alex Thompson (Lead Programmer)
            • Jordan Lee (Mechanical Design)
            • Taylor Brown (Electrical Systems)
            • Morgan Davis (Strategy and Operations)
        `
    };
</script>

<style>
    :root {
        --primary-green: #2d5a27;
        --light-green: #3a7a33;
        --background: #f5f5f0;
        --card-bg: #fff;
        --border-radius: 12px;
        --text-main: #222;
        --text-muted: #666;
    }

    .article-container {
        max-width: 800px;
        margin: 2rem auto;
        padding: 0 1rem;
    }

    .article-header {
        margin-bottom: 2rem;
    }

    .article-title {
        font-size: 2.5rem;
        color: var(--primary-green);
        margin-bottom: 1rem;
        line-height: 1.2;
    }

    .article-meta {
        color: var(--light-green);
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .article-image {
        width: 100%;
        height: 400px;
        object-fit: cover;
        border-radius: var(--border-radius);
        margin-bottom: 2rem;
    }

    .article-content {
        font-size: 1.1rem;
        line-height: 1.6;
        color: var(--text-main);
    }

    .article-content p {
        margin-bottom: 1.5rem;
    }
</style>

<div class="article-container">
    <div class="article-header">
        <h1 class="article-title">{article.title}</h1>
        <div class="article-meta">
            By {article.author} • {article.date} • {article.readTime}
        </div>
        <img class="article-image" src={article.image} alt={article.title} />
    </div>
    <div class="article-content">
        {#each article.content.split('\n') as paragraph}
            {#if paragraph.trim()}
                <p>{paragraph}</p>
            {/if}
        {/each}
    </div>
</div> 