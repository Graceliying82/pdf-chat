css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 32 32"
            style="max-height: 50px; max-width: 50px; border-radius: 50%; object-fit: cover;">
        <g fill="white"><path d="M13.472 26h5.056C19.34 26 20 25.326 20 24.5s-.66-1.5-1.472-1.5h-5.056C12.66 23 12 23.674 12 24.5s.66 1.5 1.472 1.5ZM10.5 10a4.5 4.5 0 1 0 0 9h11a4.5 4.5 0 1 0 0-9h-11Zm.75 2c.69 0 1.25.56 1.25 1.25v2.5a1.25 1.25 0 1 1-2.5 0v-2.5c0-.69.56-1.25 1.25-1.25Zm8.25 1.25a1.25 1.25 0 1 1 2.5 0v2.5a1.25 1.25 0 1 1-2.5 0v-2.5Z"/><path d="M4 4.915a1.5 1.5 0 1 0-1 0v7.355a2 2 0 0 0-1 1.728v7.004c0 .736.403 1.382 1 1.729v1.319A6.945 6.945 0 0 0 9.95 31h12.1A6.943 6.943 0 0 0 29 24.06v-1.39c.597-.347 1-.994 1-1.73v-7.01c0-.736-.403-1.383-1-1.73V5.018a1.55 1.55 0 1 0-1 0v3.396A7.017 7.017 0 0 0 21.98 5h-1.065A1.5 1.5 0 0 0 19.5 3h-7a1.5 1.5 0 0 0-1.415 2H10.03C7.47 5 5.23 6.369 4 8.414v-3.5Zm1 7.115A5.03 5.03 0 0 1 10.03 7h11.95A5.028 5.028 0 0 1 27 12.03v12.03A4.943 4.943 0 0 1 22.05 29H9.95A4.945 4.945 0 0 1 5 24.05V12.03Z"/></g></svg>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <svg 
            xmlns="http://www.w3.org/2000/svg" 
            width="256" 
            height="256" 
            viewBox="0 0 256 256"
            style="max-height: 50px; max-width: 50px; border-radius: 50%; object-fit: cover;">
            <path fill="white" d="M168 96H88a40 40 0 0 0-40 40v8a40 40 0 0 0 40 40h80a40 40 0 0 0 40-40v-8a40 40 0 0 0-40-40Zm24 48a24 24 0 0 1-24 24H88a24 24 0 0 1-24-24v-8a24 24 0 0 1 24-24h80a24 24 0 0 1 24 24Zm16-112a32.06 32.06 0 0 0-31 24H79a32 32 0 0 0-63 8v80a72.08 72.08 0 0 0 72 72h80a72.08 72.08 0 0 0 72-72V64a32 32 0 0 0-32-32Zm16 112a56.06 56.06 0 0 1-56 56H88a56.06 56.06 0 0 1-56-56V64a16 16 0 0 1 32 0a8 8 0 0 0 8 8h112a8 8 0 0 0 8-8a16 16 0 0 1 32 0Zm-120-4a12 12 0 1 1-12-12a12 12 0 0 1 12 12Zm72 0a12 12 0 1 1-12-12a12 12 0 0 1 12 12Z"/>
            </svg>
Download SVG
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''