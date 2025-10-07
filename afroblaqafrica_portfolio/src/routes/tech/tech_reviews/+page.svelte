<script>
    import tiktok_views from '$lib/assets/analytics/tiktok_views.jpg'
    import tiktok_subs from '$lib/assets/analytics/tiktok_followers.jpg'
    import yt_views from '$lib/assets/analytics/yt_views.jpg'
    import yt_subs from '$lib/assets/analytics/yt_subs.jpg'

    const tech_review_analytics = [
        {
        social_page_name: "Tiktok analytics", 
        social_page_subs : tiktok_subs,
        social_page_views : tiktok_views
        },
        {
        social_page_name: "Youtube analytics",
        social_page_views: yt_views, 
        social_page_subs : yt_subs
        }

    ]
</script>

 {#each tech_review_analytics as analytics_card_details }
    <div id="tech_review_container" class="m-5 md:w-150 my-10 mx-auto">
        <div id="tech_review_card" class="bg-gray-100 p-5 shadow-sm m-3">
            <h3 class="font-bold text-2xl">{analytics_card_details.social_page_name}</h3>
            
            <div id="card_title" class="text-sm p-4 grid grid-cols-2 gap-5">
                <img class="hover:border border-black" src={analytics_card_details.social_page_views} alt="">
                <img class="hover:border border-black" src={analytics_card_details.social_page_subs} alt="">
            </div>
        </div>
    </div>
 {/each}