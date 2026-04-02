document.addEventListener("DOMContentLoaded", () => {
    const copyBtn = document.getElementById("copy-btn");
    const bibtexCode = document.getElementById("bibtex-code");

    if (copyBtn && bibtexCode) {
        copyBtn.addEventListener("click", () => {
            const textToCopy = bibtexCode.innerText;
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalText = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
                setTimeout(() => {
                    copyBtn.innerHTML = originalText;
                }, 2000);
            }).catch(err => {
                console.error("Failed to copy text: ", err);
            });
        });
    }
});
