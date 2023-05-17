import { useNavigation, useRoute } from "@react-navigation/native"
import { useLayoutEffect } from "react"
import {View, Text, StyleSheet} from "react-native"
import {HeaderBackButton} from "@react-navigation/elements"


const ProfileDetailScreen = () => {
    const route = useRoute()
    const{profileId} = route.params
    const navigation = useNavigation()

    useLayoutEffect(()=> {
        navigation.setOptions({
            headerLeft: () => (
                <HeaderBackButton
                    tintColor="white"
                    onPress={()=> navigation.goBack()}
                />
            ) 
        })
    }, [])

    return (
        <View>
            <Text>Profile id: {profileId}</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    screen: {
        padding: 20,
    }
})

export default ProfileDetailScreen