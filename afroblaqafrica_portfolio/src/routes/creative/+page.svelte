
<script>
    const creative_details = [
        {page_name: "Documentary", 
        ahref: "/creative/documentary",
        page_brief_title:"Brief:",
        page_brief:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!",},
          {page_name: "Portaits", 
          ahref: "/creative/portraits",
        page_brief_title:"Brief:",
        page_brief:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!"},
        {page_name: "Music video", 
        ahref: "/creative/music_video",
        page_brief_title:"Brief:",
        page_brief:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!"},
        
    ]
</script>

<div id="creative_container" class="m-5 md:w-150 my-5 mx-auto">
    {#each creative_details as card_details }
        
            <div id="creative_card" class="bg-gray-100 p-5 hover:border border-black shadow-sm m-3 ">
                <h3 class="font-bold text-2xl">{card_details.page_name}</h3>

                <div id="card_title" class="text-sm p-4">
                    <h5 class="font-bold">
                        {card_details.page_brief_title}
                    </h5>
                    <p>{card_details.page_brief}</p>
                </div>
                <div id="view_portfolio_button">
                    <a href={card_details.ahref}>
                    <button class="bg-black p-2 text-white w-full hover:bg-gray-800">View portfolio</button>
                </a>
                </div>
            </div>
      
    {/each}
</div>