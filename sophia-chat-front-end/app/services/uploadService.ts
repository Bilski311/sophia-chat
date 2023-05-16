const uploadFile = (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    let response;
    fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/upload`, {
        method: 'POST',
        body: formData,
    })
    .then((res) => response = res)
    .catch((err) => console.log(err.message));

    return response;
}

export default {
    uploadFile,
}
