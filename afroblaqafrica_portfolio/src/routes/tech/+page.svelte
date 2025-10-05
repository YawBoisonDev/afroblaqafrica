<script>
    const tech_review_details = [
        {page_name: "Tech truth reviews", 
        page_ahref:"/tech/tech_reviews",
        page_mission_title:"Mission:",
        page_brief_title:"Brief:",
        page_brief:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!",
        page_mission:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!"},

          {page_name: "Full stack web developers", 
          page_ahref:"/tech/full_stack",
        page_mission_title:"Mission:",
        page_brief_title:"Brief:",
        page_brief:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!",
        page_mission:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!"}
    ]
</script>

 {#each tech_review_details as card_details }
 <a href={card_details.page_ahref}>
    <div id="tech_review_container" class="m-5">
   
        <div id="tech_review_card" class="bg-gray-100 p-5 shadow-sm m-3">
            <h3 class="font-bold text-2xl">{card_details.page_name}</h3>

            <div id="card_title" class="text-sm p-4">
                <h5 class="font-bold">
                {card_details.page_brief_title}
                </h5>
                <p>{card_details.page_brief}</p>
            </div>
            
            <div id="card_mission" class="text-sm p-4">
                <h5 class="font-bold">
                {card_details.page_mission_title}
                </h5>
                <p >{card_details.page_mission}</p>
            </div>
        </div>
    </div>
 </a>

 {/each}