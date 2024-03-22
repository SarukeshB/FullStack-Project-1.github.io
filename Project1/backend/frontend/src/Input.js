
import './Input.css'
import React, { useState } from 'react';
import axios from 'axios';

function NameForm() {
    const [id, setId] = useState('');
    const [title, setTitle] = useState('');
    const [due_date, setDueDate] = useState('');
    const [idToDelete, setIdToDelete] = useState(''); 

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            axios.post('/store-name/', { id, title, due_date })
            alert('Data stored successfully!');
            setId('');
            setTitle('');
            setDueDate('');
        } catch (error) {
            console.error('Error storing name:', error);
            alert('Failed to store name. Please try again.');
        }
    };

    const handleDelete = async () => {
        try {
            axios.post('/delete-data/', { id: idToDelete })
            alert('Data deleted successfully!');
            setIdToDelete(''); 
        } catch (error) {
            console.error('Error deleting data:', error);
            alert('Failed to delete data. Please try again.');
        }
    };

    return (
        <div>
            <h2>Create your To Do List ✍🏻</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Add New task <br></br><br></br>
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
            <form>
                <div>
                    
                    <label>
                        Remove Completed Task
                        <input className='Complete-label' placeholder='Enter ID to Remove' type="text" value={idToDelete} onChange={(e) => setIdToDelete(e.target.value)} />
                    </label>
                    <button className='button-38' onClick={handleDelete}>Completed</button>
                </div>
            </form>
        </div>
    );
}

export default NameForm;
