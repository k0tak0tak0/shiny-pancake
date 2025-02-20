# shiny-pancake
Call the bsky API to get an account follower count.

The API documentation has no explanation of how 'app.bsky.graph.get_followers' works, so I don't really understand what's happening.

From experimenting I concluded that calling this function returns only accounts you haven't blocked.
