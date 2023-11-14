<script>
  function addCopyButtonToCodeBlock(codeBlock) {
    // Create a "Copy" button element
    var copyButton = document.createElement('button');
    copyButton.className = 'copy-button';
    copyButton.textContent = 'Copy';

    // Add an event listener to copy the code when the button is clicked
    copyButton.addEventListener('click', function() {
        // Find the code element within the code block
        var codeElement = codeBlock.querySelector('code');
        
        // Create a temporary textarea element to copy the code
        var textarea = document.createElement('textarea');
        textarea.value = codeElement.textContent;
        document.body.appendChild(textarea);

        // Select and copy the code
        textarea.select();
        document.execCommand('copy');

        // Remove the temporary textarea
        document.body.removeChild(textarea);

        // Change the button text temporarily to indicate success
        copyButton.textContent = 'Copied!';
        setTimeout(function () {
            copyButton.textContent = 'Copy';
        }, 2000); // Reset to 'Copy' after 2 seconds
    });

    // Append the "Copy" button to the code block
    codeBlock.appendChild(copyButton);
}

// Get all codehilite div elements
var codeBlocks = document.querySelectorAll('.codehilite');

// Add the "Copy" button to each code block
codeBlocks.forEach(function(codeBlock) {
    addCopyButtonToCodeBlock(codeBlock);
});

    
</script>

