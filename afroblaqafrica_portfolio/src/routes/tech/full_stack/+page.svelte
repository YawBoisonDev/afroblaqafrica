
<script>
    const full_stack_details = [
        {page_name: "www.afroblaqfrica.com", 
        ahref: "",
        page_brief_title:"Brief:",
        page_brief:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!",},
          {page_name: "www.gimmiedeal.com", 
          ahref: "",
        page_brief_title:"Brief:",
        page_brief:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!"},
        {page_name: "www.strugglingcreative.com", 
        ahref: "",
        page_brief_title:"Brief:",
        page_brief:"Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates magni inventore minima, distinctio, fugiat odio quam aliquam ratione eius dolorum blanditiis. Illo sequi dolorum voluptatum pariatur, vel quae laudantium deserunt!"}
    ]
</script>

<div id="full_stack_container" class="m-5 md:w-150 my-10 mx-auto">
    {#each full_stack_details as card_details }
        <a href={card_details.ahref}>
            <div id="full_stack_card" class="bg-gray-100 p-5 shadow-sm m-3 ">
                <h3 class="font-bold text-2xl">{card_details.page_name}</h3>

                <div id="card_title" class="text-sm p-4">
                    <h5 class="font-bold">
                        {card_details.page_brief_title}
                    </h5>
                    <p>{card_details.page_brief}</p>
                </div>
                
            </div>
        </a>
    {/each}
</div>