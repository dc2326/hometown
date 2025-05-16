<script>
    let article = {
        title: 'Robotics Club Open House Next Week',
        date: 'May 6, 2024',
        author: 'Michael Chen',
        readTime: '3 min read',
        content: `
            Following their recent state championship victory, the Hometown High Robotics Team is opening its doors to new members with a special open house event next week. The event, scheduled for May 15th from 4:00 PM to 7:00 PM, will give students and their families a chance to learn about the program and see the championship-winning robot in action.

            "We want to share our passion for robotics with more students," says team captain Sarah Martinez. "No prior experience is necessary - we'll teach you everything you need to know."

            The open house will feature:
            • Live demonstrations of the championship robot
            • Hands-on activities for beginners
            • Information about the team's competition schedule
            • Meet-and-greet with current team members
            • Q&A session with team advisors

            The robotics program has grown significantly in recent years, thanks to increased community support and the success of its students. The team now has access to state-of-the-art equipment and a dedicated workspace in the school's new STEM wing.

            "We're looking for students who are curious, creative, and willing to work as part of a team," says team advisor Mr. James Wilson. "The skills you learn in robotics - problem-solving, programming, engineering - are valuable in any career path."

            Interested students can sign up for the open house through the school's website or by contacting the STEM department. The team is particularly encouraging girls and underrepresented groups in STEM to attend.

            For more information, visit www.hometownhigh.edu/robotics or call the STEM department at (555) 987-6543.
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
    </div>
    <div class="article-content">
        {#each article.content.split('\n') as paragraph}
            {#if paragraph.trim()}
                <p>{paragraph}</p>
            {/if}
        {/each}
    </div>
</div> 