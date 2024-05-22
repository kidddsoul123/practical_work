% rebase('layout.tpl', title='Partner companies', year=year)

<div class="jumbotron" style="background-color:#282a36">
    <h1 style="color:white">Our partner</h1>
    <p style="color:white" class="lead">Our partner companies are represented on this page of the website. 
    If you are our partner, you can send a request to add your company to the site page. To do this, enter the 
    following information on the form below: 1. The name of the company 
2. Description
3. Contacts
4. The start date of the work.
5. Name of the CEO 
6. Photography</p>
</div>

<h2 style="color:white">List of our partners:</h2>

<h3 style="color:white"> Add a partner-company </h3>
        <form action="/home" method="post">

        <p><input type="text" size="50" name="Company_Name" placeholder = "Enter the name of the company"></p>

        <p><textarea rows="1" cols="50" name="Description" oninput="autoResize(this)" placeholder= "Enter a description of your company"></textarea> </p>
        <style>
            textarea
            { resize: none; } 
        </style>

        <p><textarea rows="1" cols="50" name="Contacts" oninput="autoResize(this)" placeholder= "Enter the contacts to get in touch with you"></textarea> </p>

        <p><input type="date" size="50" name="Date_Start" lang="en"</p>

        <p><input type="text" size="50" name="CEO_Name" placeholder = "Enter the CEO name"></p>

        <p><input type="submit" value="Add" class="btn btn-default" ></p>

</form>

   <script>
    function autoResize(textarea) {
        textarea.style.height = 'auto'; // Reset height
        textarea.style.height = (textarea.scrollHeight) + 'px'; // Set height to content height
    }
</script>