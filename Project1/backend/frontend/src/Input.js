import './Input.css'
import React, { useState } from 'react';
import axios from 'axios';

function NameForm() {
    const [name, setName] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await axios.post('http://localhost:8000/store-name/', { name });
            alert('Name stored successfully!');
            setName('');
        } catch (error) {
            console.error('Error storing name:', error);
            alert('Failed to store name. Please try again.');
        }
    };
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Get In Touch ⬇️ <br></br><br></br>
                    <input type="text" placeholder='Enter Your Name' value={name} onChange={(e) => setName(e.target.value)} />
                </label>
                <button className='button-38' type="submit">Submit</button>
            </form>
        </div>
    );
}

export default NameForm;

