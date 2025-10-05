<script>
    const documentary_links = [
        {id: 'fKMe2PyPTDE?si=WxEsmQW7igJphSBd'},
        {id:"vX9YMmoTvXg?si=zmkTVu_Rm3JQ-RaQ"},
        {id: 'XuBhPjcRdIw?si=Im3bk-Qk8Ge73EoL'},
        {id:'-YYnHHcs3o4?si=8ZZcbPp8ZGCXvxQs'},
        {id:'AVYWLZ-6VpI?si=oRm-Db78eMkIgmdo'},
        {id:'7gC1btFIyzg?si=NfAChm9-F6bCs9Zp'},
        {id: 'spn8df4ULlo?si=jxuOHmbV8M3v2srY'},
        {id: 'eE03RM8vkj4?si=-Xa8Y7ZDMdV3ryAw'},
        {id:'lTeWFGuKkJc?si=AqFwdPCGHqlyYsPS'},
        {id:'xpsY20gxtHg?si=NBOFwxaCMsAzjYjW'},
        {id:'CsmirZE9T3s?si=vNx9s3bSZid_3gSp'},
        {id:'OJYWeDNqZ5E?si=xvg4LbXub7vhKw6U'},
        {id:'khCUwx1jzSk?si=eTxP93sjxp8xps86'},
        {id:'IU2KysWlvwk?si=ZzHn8hzMuX3wF3ld'},
        {id:'videoseries?si=gmuQQ2YrqzzEjhPu&amp;list=PLUlbK55IQybiBWmK116p270lDOzbP9lLu'}


    ]
</script>


<div id="documentary_card" class="grid grid-cols-1 gap-4 mx-5 my-auto">
    {#each documentary_links as docu_link}
        <iframe
            width="450"
            height="253"
            src={`https://www.youtube.com/embed/${docu_link.id}`}
            title="YouTube video player"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerpolicy="strict-origin-when-cross-origin"
            allowfullscreen>
        </iframe>
    {/each}
</div>