import axios from 'axios';

export default async function upload(filename, image) {
    const postBody = {
        image: image,
        filename: filename
    }

    try {
        const response = await axios.post('https://72gd4ty269.execute-api.ca-central-1.amazonaws.com/image', postBody);
        return response.data.filename;
    } catch(e) {
        console.error(e)
        alert(error.response.data.error);
        return null;
    }
}


