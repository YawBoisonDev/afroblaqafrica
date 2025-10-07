<script lang="ts">
    let get_email:String = $state("")
    let get_message:String = $state("")

    function handle_Submit(e:Event):void{
        e.preventDefault()

    }
    
  
</script>

<form action="https://api.web3forms.com/submit" method="POST" onsubmit={handle_Submit} >
    <div id="form_id" class="grid grid-cols-1 gap-2 bg-gray-200 w-100 p-5 mx-auto my-85">
        <input type="hidden" name="access _key" value="eca1a69f-3326-4d72-8a43-a7f79882abf5">
    <label for="email">
        <input placeholder="Enter your email" class="border border-black w-full p-2" type="email" name="email" bind:value={get_email}>
    </label>

    <label for="message">
        <textarea placeholder="Enter your message" class="border border-black w-full h-60 p-2" bind:value={get_message} >
        </textarea>
    </label>
    <button class="bg-black p-2 text-white w-full hover:bg-gray-800" type="submit">Send mail</button>
    </div>
    
</form>