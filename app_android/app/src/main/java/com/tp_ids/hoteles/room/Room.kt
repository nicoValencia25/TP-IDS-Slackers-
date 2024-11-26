package com.tp_ids.hoteles.room

data class Room(
    // General
    val id: Int,
    val name: String,
    val imageLink: String,
    val description: String,
    val guests: Int,
    val priceAdult: Int,
    val priceChildren: Int,
    // Hotel
    val floor: Int,
    val number: Int
)