import React from 'react';
import Calculator from '../containers/Calculator';
import {render, fireEvent} from '@testing-library/react';

describe('Calculator', () => {
  let container;
  let button0;
  let button1;
  let button2;
  let button3;
  let button4;
  let button5;
  let button6;
  let button7;
  let button8;
  let button9;
  let operatorAdd;
  let operatorEquals;
  let operatorSubtract;
  let operatorMultiply;
  let operatorDivide;
  let runningTotal;
  let clear;
  
  beforeEach(() => {
    container = render(<Calculator/>)
    button0 = container.getByTestId('number0');
    button1 = container.getByTestId('number1');
    button2 = container.getByTestId('number2');
    button3 = container.getByTestId('number3');
    button4 = container.getByTestId('number4');
    button5 = container.getByTestId('number5');
    button6 = container.getByTestId('number6');
    button7 = container.getByTestId('number7');
    button8 = container.getByTestId('number8');
    button9 = container.getByTestId('number9');
    operatorAdd = container.getByTestId('operator-add');
    operatorSubtract = container.getByTestId('operator-subtract');
    operatorMultiply = container.getByTestId('operator-multiply');
    operatorDivide = container.getByTestId('operator-divide');
    operatorEquals = container.getByTestId('operator-equals');
    runningTotal = container.getByTestId('running-total');
    clear = container.getByTestId('clear');
  })

  it('should change running total on number enter', () => {
    fireEvent.click(button4);
    expect(runningTotal.textContent).toEqual('4');
  })

  it('should be able to add numbers with calculator.add()', () => {
    fireEvent.click(button1);
    fireEvent.click(operatorAdd);
    fireEvent.click(button4);
    fireEvent.click(operatorEquals)
    expect(runningTotal.textContent).toEqual('5')
  })

  it('should be able to subtract numbers with calculator.subtract()', () => {
    fireEvent.click(button7);
    fireEvent.click(operatorSubtract);
    fireEvent.click(button4);
    fireEvent.click(operatorEquals);
    expect(runningTotal.textContent).toEqual('3')
  })

  it('should be able to multiply numbers with calculator.multiply()', () => {
    fireEvent.click(button5);
    fireEvent.click(operatorMultiply);
    fireEvent.click(button3);
    fireEvent.click(operatorEquals);
    expect(runningTotal.textContent).toEqual('15')
  })

  it('should be able to divide numbers with calculator.divide()', () => {
    fireEvent.click(button2);
    fireEvent.click(button1);
    fireEvent.click(operatorDivide);
    fireEvent.click(button7);
    fireEvent.click(operatorEquals);
    expect(runningTotal.textContent).toEqual('3')
  })
  
  it('should be able to concatenate multiple number clicks with calculator.numberClick()', () => {
    fireEvent.click(button4);
    fireEvent.click(button2);
    expect(runningTotal.textContent).toEqual('42')
  })

  it('should be able to chain multiple operations together', () => {
    fireEvent.click(button6);
    fireEvent.click(operatorMultiply);
    fireEvent.click(button7);
    fireEvent.click(operatorMultiply);
    fireEvent.click(button1);
    fireEvent.click(button0);
    fireEvent.click(button0);
    fireEvent.click(button0);
    fireEvent.click(operatorAdd);
    fireEvent.click(button6)
    fireEvent.click(button9)
    fireEvent.click(operatorEquals);
    expect(runningTotal.textContent).toEqual('42069')
  })

  it('should clear the running total without affecting calculation', () => {
    fireEvent.click(button6);
    fireEvent.click(operatorMultiply);
    fireEvent.click(button7);
    fireEvent.click(operatorMultiply);
    fireEvent.click(button1);
    fireEvent.click(button0);
    fireEvent.click(button0);
    fireEvent.click(button0);
    fireEvent.click(clear);
    fireEvent.click(button8)
    fireEvent.click(operatorEquals);
    expect(runningTotal.textContent).toEqual('336')
  })

})
