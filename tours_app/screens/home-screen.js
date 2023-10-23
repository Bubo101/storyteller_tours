import {View, Text, StyleSheet, Button} from "react-native"
import { useEffect, useState } from "react"
import EventList from "../components/events/event-list"
import { useNavigation } from "@react-navigation/native"

const HomeScreen = () => {
    const navigation = useNavigation()
    const [data, setData] = useState([])
    const [refresh, setRefresh] = useState(false)

    const handleRefresh = () => {
        console.log('refreshing')
        setRefresh(prevState => !prevState)
    }

    useEffect(()=> {
        fetchData()
    }, [refresh])
    // every time refresh changes it will run useEffect again

    const fetchData = async() => {
        const response = await fetch('http://localhost:8000/tours_api/tours/')
        const data = await response.json()
        setData(data)

    }
    return (
        <View style={styles.screen}>
            <Button onPress={() => navigation.navigate('New Event')} title="add new Event" />
            <EventList data={data} onRefresh={handleRefresh} />
        </View>
    )
}

const styles = StyleSheet.create({
    screen: {
        padding: 20,
    }
})

export default HomeScreen