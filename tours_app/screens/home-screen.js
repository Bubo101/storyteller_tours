import {View, Text, StyleSheet, Button} from "react-native"
import { useEffect, useState } from "react"
import EventList from "../components/events/event-list"

const HomeScreen = () => {
    const [data, setData] = useState([])
    useEffect(()=> {
        fetchData()
    }, [])

    const fetchData = async() => {
        const response = await fetch('http://localhost:8000/api/storyteller_app/')
        const data = await response.json()
        setData(data)

    }
    return (
        <View style={styles.screen}>
            <EventList data={data} />
        </View>
    )
}

const styles = StyleSheet.create({
    screen: {
        padding: 20,
    }
})

export default HomeScreen