<script lang="ts">
    import axios from "axios";
    let get_email:string = $state("")
    let get_message:string = $state("")
    let get_name:string = $state("")
    let error_message:string = $state("")
    let success_message:string = $state("")

    async function handle_Submit(event:Event) {
        event.preventDefault();
        console.log("Name:", get_name);
        console.log("Email:", get_email);
        console.log("Message:", get_message);
        // Here you can add code to send the form data to your server or an API

        try{
            await axios.post('http://localhost:8000/contact', {
                Name: get_name,
                Email: get_email,
                Message: get_message
  
            })
            get_email = ""
            get_name= ""
            get_message=""
            success_message = "Your message has been sent successfully!";}
        catch(error){
            error_message = "There was an error sending your message. Please try again later."
            console.error("Error sending message:", error);
            return;
        }
        

    }
    
  
</script>

<form onsubmit={handle_Submit} >
    <div id="form_id" class="grid grid-cols-1 gap-2 bg-gray-200 w-100 p-5 mx-auto my-85">
    <label for="name">
                <input placeholder="Enter your name" class="border border-black w-full p-2" type="text" name="name" bind:value={get_name}>
    </label>
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
