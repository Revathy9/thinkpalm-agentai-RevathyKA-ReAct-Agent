import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const sendMessage = async (message) => {
    const response = await axios.post(
        `${BASE_URL}/chat`,
        {
            message: message
        }
    );
    return response.data;
};

export const fetchMemory = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/memory`);
        return response.data;
    } catch (error) {
        console.error("Error fetching memory:", error);
        return {};
    }
};
