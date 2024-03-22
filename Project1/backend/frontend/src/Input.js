
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Input.css';

function NameForm() {
    const [id, setId] = useState('');
    const [title, setTitle] = useState('');
    const [due_date, setDueDate] = useState('');
    const [idToDelete, setIdToDelete] = useState('');
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await axios.get('/get-data/');
            setTasks(response.data.split('\n'));
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await axios.post('/store-name/', { id, title, due_date });
            alert('Data stored successfully!');
            setId('');
            setTitle('');
            setDueDate('');
            fetchData();
        } catch (error) {
            console.error('Error storing name:', error);
            alert('Failed to store name. Please try again.');
        }
    };

    const handleDelete = async () => {
        try {
            await axios.post('/delete-data/', { id: idToDelete });
            alert('Data deleted successfully!');
            setIdToDelete('');
            fetchData();
        } catch (error) {
            console.error('Error deleting data:', error);
            alert('Failed to delete data. Please try again.');
        }
    };

    return (
        <div className="App-header">
            <h2>Create your To Do List ✍🏻</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Add New task <br /><br />
                    <input className="Complete-label" type="text" placeholder='Enter ID' value={id} onChange={(e) => setId(e.target.value)} />
                </label>
                <label>
                    <input className="Complete-label" type="text" placeholder='Enter title of Task' value={title} onChange={(e) => setTitle(e.target.value)} />
                </label>
                <label>
                    <input className="Complete-label" type="text" placeholder='Enter Due Date' value={due_date} onChange={(e) => setDueDate(e.target.value)} />
                </label>
                <button className="button-38" type="submit">Submit</button>
            </form>

            <h2>Task's To Complete ☑️</h2>

            <div className='task-to'>
                <ul>
                    {tasks.map((task, index) => (
                        <li key={index}>{task && (
                            <div className='output'>
                                <div> {task.split('\n')[0]}</div>
                                <div> {task.split('\n')[1]}</div>
                                <div> {task.split('\n')[2]}</div>
                            </div>
                        )}</li>
                    ))}

                </ul>
            </div>

            <form>
                <div>
                    <label>
                        Remove Completed Task
                        <input className="Complete-label" placeholder='Enter ID to Remove' type="text" value={idToDelete} onChange={(e) => setIdToDelete(e.target.value)} />
                    </label>
                    <button className="button-38" onClick={handleDelete}>Completed</button>
                </div>
            </form>
        </div>
    );
}

export default NameForm;
