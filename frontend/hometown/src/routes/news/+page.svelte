<script>
    // Main article (headline left, image right)
    let mainArticle = {
        title: 'Park Revitalization Project Underway',
        excerpt: 'The town has begun a major revitalization of the central park, adding new walking trails, gardens, and a playground. Community members are invited to participate in volunteer days throughout the summer.',
        date: 'May 15, 2024',
        readTime: '5 min read',
        image: '/park.jpg',
        link: '/news/park-revitalization'
    };

    // Sidebar articles (vertical stack)
    let sidebarArticles = [
        {
            title: 'Robotics Team Wins State Championship',
            excerpt: 'The Hometown High Robotics Team took first place at the state competition, impressing judges with their innovative design and teamwork.',
            date: 'May 10, 2024',
            readTime: '4 min read',
            image: '/robot.jpg',
            link: '/news/robotics-championship'
        },
        {
            title: 'Park Volunteer Day Announced',
            excerpt: 'Join your neighbors for a day of planting and cleanup at the park this Saturday. All ages welcome!',
            date: 'May 8, 2024',
            readTime: '2 min read',
            link: '/news/park-volunteer-day'
        }
    ];

    // Lower row articles (no images)
    let lowerArticles = [
        {
            title: 'Robotics Club Open House Next Week',
            excerpt: 'Interested in robotics? The club is hosting an open house for new members. No experience required.',
            date: 'May 6, 2024',
            readTime: '3 min read',
            link: '/news/robotics-open-house'
        },
        {
            title: 'Park Receives Green Space Grant',
            excerpt: 'A new grant will fund additional trees and benches in the park, making it more accessible for everyone.',
            date: 'May 4, 2024',
            readTime: '2 min read',
            link: '/news/park-grant'
        }
    ];

    function handleClick(link) {
        window.location.href = link;
    }
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
    --serif: 'Georgia', 'Times New Roman', Times, serif;
    --sans-serif: 'Inter', 'Segoe UI', Arial, sans-serif;
}

body, .news-bg {
    background: var(--background);
    color: var(--text-main);
    font-family: var(--serif);
}

.news-main {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 1rem;
}

.nyt-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 2.5rem;
}

.nyt-main-article {
    display: flex;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 2.5rem;
    margin-bottom: 2.5rem;
    gap: 2rem;
    cursor: pointer;
}
.nyt-main-text {
    flex: 2;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-right: 1.5rem;
}
.nyt-main-title {
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--primary-green);
    margin-bottom: 1rem;
    line-height: 1.2;
    letter-spacing: -0.02em;
    max-width: 90%;
}
.nyt-main-excerpt {
    font-size: 1.15rem;
    color: var(--text-main);
    margin-bottom: 1.5rem;
    line-height: 1.5;
    max-width: 95%;
}
.nyt-main-meta {
    color: var(--light-green);
    font-size: 0.95rem;
    font-weight: 600;
    letter-spacing: 0.02em;
}
.nyt-main-img {
    flex: 1.2;
    min-width: 260px;
    max-width: 400px;
    height: 260px;
    object-fit: cover;
    border-radius: var(--border-radius);
    box-shadow: 0 2px 12px rgba(44,62,80,0.10);
}

.nyt-sidebar {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}
.nyt-side-article {
    display: flex;
    gap: 1.2rem;
    cursor: pointer;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 1.5rem;
    margin-bottom: 1.5rem;
}
.nyt-side-img {
    width: 110px;
    height: 90px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 1px 6px rgba(44,62,80,0.08);
}
.nyt-side-content {
    flex: 1;
    padding-right: 1rem;
}
.nyt-side-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--primary-green);
    margin-bottom: 0.5rem;
    line-height: 1.3;
    letter-spacing: -0.01em;
}
.nyt-side-excerpt {
    font-size: 0.98rem;
    color: var(--text-main);
    margin-bottom: 0.6rem;
    line-height: 1.4;
}
.nyt-side-meta {
    color: var(--light-green);
    font-size: 0.85rem;
    font-weight: 600;
}

.nyt-lower-row {
    display: flex;
    gap: 2.5rem;
    margin-top: 3rem;
    border-top: 1px solid #e0e0e0;
    padding-top: 2.5rem;
}
.nyt-lower-article {
    flex: 1;
    cursor: pointer;
    padding-right: 1.5rem;
}
.nyt-lower-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--primary-green);
    margin-bottom: 0.5rem;
    line-height: 1.3;
    letter-spacing: -0.01em;
}
.nyt-lower-excerpt {
    font-size: 0.97rem;
    color: var(--text-main);
    margin-bottom: 0.5rem;
    line-height: 1.4;
}
.nyt-lower-meta {
    color: var(--light-green);
    font-size: 0.82rem;
    font-weight: 600;
}

@media (max-width: 900px) {
    .nyt-grid {
        grid-template-columns: 1fr;
    }
    .nyt-main-article {
        flex-direction: column;
        align-items: flex-start;
    }
    .nyt-main-img {
        width: 100%;
        max-width: 100%;
        height: 220px;
    }
    .nyt-sidebar {
        flex-direction: row;
        gap: 1.5rem;
    }
    .nyt-side-article {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.7rem;
        width: 100%;
    }
    .nyt-side-img {
        width: 100%;
        height: 120px;
    }
}
@media (max-width: 600px) {
    .nyt-lower-row {
        flex-direction: column;
        gap: 1.5rem;
    }
}
</style>

<div class="news-bg">
    <div class="news-main">
        <h1 style="text-align: center; color: var(--primary-green); font-size: 2.5rem; margin-bottom: 2rem; font-weight: 700;">All Your Local News in One Place</h1>
        <div class="nyt-grid">
            <div>
                <div class="nyt-main-article" on:click={() => handleClick(mainArticle.link)}>
                    <div class="nyt-main-text">
                        <div class="nyt-main-title">{mainArticle.title}</div>
                        <div class="nyt-main-excerpt">{mainArticle.excerpt}</div>
                        <div class="nyt-main-meta">{mainArticle.date} &bull; {mainArticle.readTime}</div>
                    </div>
                    <img class="nyt-main-img" src={mainArticle.image} alt={mainArticle.title} />
                </div>
                <div class="nyt-lower-row">
                    {#each lowerArticles as article}
                        <div class="nyt-lower-article" on:click={() => handleClick(article.link)}>
                            <div class="nyt-lower-title">{article.title}</div>
                            <div class="nyt-lower-excerpt">{article.excerpt}</div>
                            <div class="nyt-lower-meta">{article.date} &bull; {article.readTime}</div>
                        </div>
                    {/each}
                </div>
            </div>
            <div class="nyt-sidebar">
                {#each sidebarArticles as article}
                    <div class="nyt-side-article" on:click={() => handleClick(article.link)}>
                        {#if article.image}
                            <img class="nyt-side-img" src={article.image} alt={article.title} />
                        {/if}
                        <div class="nyt-side-content">
                            <div class="nyt-side-title">{article.title}</div>
                            <div class="nyt-side-excerpt">{article.excerpt}</div>
                            <div class="nyt-side-meta">{article.date} &bull; {article.readTime}</div>
                        </div>
                    </div>
                {/each}
            </div>
        </div>
    </div>
</div>
