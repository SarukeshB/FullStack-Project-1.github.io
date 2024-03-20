//                                                                      SARUKESH BOOMINATHAN

import './Input.css'
import React, { useState } from 'react';
import axios from 'axios';

function NameForm() {
    const [id, setId] = useState('');
    const [title, setTitle] = useState('');
    const [due_date, setDueDate] = useState('');
    const [submittedData, setSubmittedData] = useState(null);
    


    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            axios.post('/store-name/', { id, title, due_date })
            alert('Data stored successfully!');
            setSubmittedData({ id, title, due_date });
            setId('');
            setTitle('');
            setDueDate('');
        } catch (error) {
            console.error('Error storing name:', error);
            alert('Failed to store name. Please try again.');
        }
    };
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    ⬇️ To-Do-List ⬇️ <br></br><br></br>
                    <input type="text" placeholder='Enter ID' value={id} onChange={(e) => setId(e.target.value)} />
                </label>
                <label>
                    <input type="text" placeholder='Enter title of Task' value={title} onChange={(e) => setTitle(e.target.value)} />
                </label>
                <label>
                    <input type="text" placeholder='Enter Due Date' value={due_date} onChange={(e) => setDueDate(e.target.value)} />
                </label>
                <button className='button-38' type="submit">Submit</button>
            </form>
             {/* Display submitted data below the input box */}
             {submittedData && (
                <div className="submitted-data" style={{ marginTop: '100px', marginBottom: '100px' }}>
                    <h2>⬇️ TASK TO DO ⬇️</h2>
                    <p>ID: {submittedData.id}</p>
                    <p>Title: {submittedData.title}</p>
                    <p>Due Date: {submittedData.due_date}</p>
                </div>
            )}
        </div>
    );
}

export default NameForm;

